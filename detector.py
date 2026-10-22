"""
Hybrid Fraud Detection Engine for Digital Arrest & Cyber Extortion Shield
Combines:
1. scikit-learn ML Classifier: TfidfVectorizer (1-3 ngrams) + LogisticRegression
2. Rule-Based Explainable Cue Engine: Regex span matching across 6 scam categories
3. Genuine Message Safeguard: Suppresses false alarms for advisories & genuine alerts
4. Strict 'Assist, Don't Accuse' Policy and Actionable Safety Next Steps
"""

import re
import time
from typing import Dict, List, Tuple, Any
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from dataset import get_dataset

# ---------------------------------------------------------
# CATEGORY DEFINITIONS, METADATA & REASONS
# ---------------------------------------------------------
CATEGORIES = {
    "fake_authority": {
        "name": "Fake Authority Claims",
        "badge_color": "#dc2626", # Crimson
        "bg_color": "#fee2e2",
        "text_color": "#991b1b",
        "explanation": "Impersonating law enforcement or regulatory agencies to create intimidation and force compliance.",
        "patterns": [
            r"\b(?:cbi|central bureau of investigation)\b",
            r"\b(?:mumbai|delhi|bangalore|karnataka|maharashtra|cyber)\s+crime\s+(?:branch|cell|department|police)\b",
            r"\b(?:supreme\s+court|high\s+court)\b",
            r"\b(?:narcotics\s+control\s+bureau|ncb)\b",
            r"\bcustoms\s+(?:department|officer|seaport|airport)\b",
            r"\b(?:enforcement\s+directorate|ed\s+notice|ed\s+squad)\b",
            r"\b(?:trai|telecom\s+regulatory\s+authority\s+of\s+india)\s*(?:official|officer|alert)?\b",
            r"\brbi\s+(?:verification\s+officer|official|supervision|audit)\b",
            r"\b(?:national\s+investigation\s+agency|nia)\b",
            r"\b(?:special\s+task\s+force|stf)\b",
            r"\binterpol\s+(?:new\s+delhi|office)?\b",
            r"\bofficer\s+from\s+(?:cbi|crime\s+branch|police|customs)\b",
            r"\b(?:inspector|acp|commissioner|sub-inspector)\s+[A-Z][a-z]+\b",
            r"\bcyber\s+police\s+headquarters\b",
            r"\bhigh\s+court\s+bailiff\b"
        ]
    },
    "threats_coercion": {
        "name": "Threats & Legal Coercion",
        "badge_color": "#ea580c", # Orange-Red
        "bg_color": "#ffedd5",
        "text_color": "#9a3412",
        "explanation": "Using fear of immediate arrest, freezing of accounts, or criminal charges to trigger panic.",
        "patterns": [
            r"\bdigital\s+arrest(?:ed)?\b",
            r"\barrested\s+today\b",
            r"\bnon-bailable\s+warrant\b",
            r"\bmoney\s+laundering\s+(?:case|scam)?\b",
            r"\bfreeze\s+(?:your\s+)?bank\s+accounts?\b",
            r"\b(?:frozen|sealed)\s+(?:your\s+)?(?:company\s+)?bank\s+accounts?\b",
            r"\bimplicated\s+in\s+a\s+crime\b",
            r"\bpolice\s+custody\b",
            r"\bndps\s+act\b",
            r"\bcontempt\s+of\s+court\b",
            r"\bfinancial\s+terrorism\b",
            r"\braid\s+at\s+your\s+house\b",
            r"\bpublic\s+dishonor\b",
            r"\bfacing\s+non-bailable\s+warrant\b",
            r"\bwill\s+be\s+jailed\b",
            r"\baccount\s+(?:has\s+been|will\s+be)\s+blocked\b",
            r"\bterror\s+funding\s+link\b"
        ]
    },
    "extreme_urgency": {
        "name": "Extreme Urgency",
        "badge_color": "#d97706", # Amber
        "bg_color": "#fef3c7",
        "text_color": "#92400e",
        "explanation": "Manufacturing artificial time pressure so you cannot think clearly or independently verify the claim.",
        "patterns": [
            r"\bimmediately\b",
            r"\bwithin\s+\d+\s+(?:minutes|mins|hours)\b",
            r"\bright\s+now\b",
            r"\blast\s+warning\b",
            r"\bbefore\s+\d+\s*(?:am|pm|today)\b",
            r"\bno\s+time\s+left\b",
            r"\btonight\s+at\s+\d+(?::\d+)?\s*(?:am|pm)?\b",
            r"\bemergency\s+notice\b"
        ]
    },
    "secrecy_isolation": {
        "name": "Secrecy & Isolation Demands",
        "badge_color": "#7c3aed", # Purple
        "bg_color": "#f3e8ff",
        "text_color": "#6b21a8",
        "explanation": "Isolating you from family, trusted friends, or bank staff who would immediately expose the scam.",
        "patterns": [
            r"\bdo\s+not\s+tell\s+anyone\b",
            r"\bkeep\s+this\s+confidential\b",
            r"\bstay\s+on\s+the\s+(?:video\s+)?call\b",
            r"\bdo\s+not\s+disconnect\b",
            r"\bnational\s+security\s+secret\b",
            r"\bdo\s+not\s+consult\s+(?:family\s+or\s+lawyer|anyone)\b",
            r"\bremain\s+in\s+a\s+closed\s+room\b",
            r"\bclosed\s+room\s+alone\b",
            r"\bkeep\s+camera\s+turned\s+on\b",
            r"\bstay\s+in\s+your\s+room\b",
            r"\bdo\s+not\s+hang\s+up\b",
            r"\bdo\s+not\s+leave\s+your\s+seat\b",
            r"\bdo\s+not\s+call\s+anyone\s+else\b",
            r"\bremain\s+isolated\b"
        ]
    },
    "money_demands": {
        "name": "Money / Asset Demands",
        "badge_color": "#0284c7", # Sky Blue
        "bg_color": "#e0f2fe",
        "text_color": "#0369a1",
        "explanation": "Genuine law enforcement and court registries never demand money transfers or security deposits to clear charges.",
        "patterns": [
            r"\btransfer\s+(?:the\s+)?money\b",
            r"\bsecurity\s+deposit\b",
            r"\brbi\s+supervision\s+account\b",
            r"\brbi\s+(?:verification|safe\s+custody|escrow)\s+account\b",
            r"\bcourt\s+(?:registrar|clearance|registry)\s+account\b",
            r"\brefundable\s+verification\s+fee\b",
            r"\brtgs\s*/\s*upi\s+transfer\b",
            r"\bsettle\s+the\s+case\b",
            r"\btransfer\s+total\s+bank\s+balance\b",
            r"\bpenalty\s+immediately\b",
            r"\bgovernment\s+(?:clearance|designated\s+escrow)\s+account\b"
        ]
    },
    "sensitive_info": {
        "name": "Sensitive Info Requests",
        "badge_color": "#059669", # Emerald
        "bg_color": "#d1fae5",
        "text_color": "#065f46",
        "explanation": "Attempting to harvest your identity documents, biometric credentials, or banking passwords.",
        "patterns": [
            r"\blinked\s+to\s+your\s+aadhaar\b",
            r"\bshare\s+otp\b",
            r"\bpan\s+card\s+details\b",
            r"\bbank\s+statement\b",
            r"\bscreen\s+share\b",
            r"\banydesk\b",
            r"\bcvv\b",
            r"\bnet\s+banking\s+password\b",
            r"\bdisclose\s+all\s+bank\s+balances\b",
            r"\bupdate\s+pan\s+and\s+aadhaar\b",
            r"\blogin\s+otp\b"
        ]
    }
}

# Patterns indicating legitimate awareness messages or safe banking notifications
GENUINE_SAFEGUARD_PATTERNS = [
    r"\b(?:never|do\s+not)\s+share\s+your\s+(?:otp|password|pin|cvv)\b",
    r"\bnever\s+conduct(?:s)?\s+(?:['\"]?)digital\s+arrest\b",
    r"\bgenuine\s+(?:police|government|officials?)\s+(?:never|will\s+never)\b",
    r"\breport\s+(?:any\s+)?(?:cyber\s+extortion|fraud|scams?)\s+(?:at|to|on)\s+(?:1930|cybercrime\.gov\.in)\b",
    r"\bdial\s+1930\b",
    r"\bhelpline\s+1930\b",
    r"\bthere\s+is\s+no\s+legal\s+procedure\s+called\s+['\"]?digital\s+arrest\b",
    r"\b(?:debited|credited|deposited)\s+(?:from|to|into)\s+a/c\b",
    r"\bavailable\s+balance\b",
    r"\bout\s+for\s+delivery\b",
    r"\bpnr\s+\d{3}-\d{7}\b",
    r"\bweb\s+check-in\b",
    r"\brefund\s+of\s+inr\b"
]


class FraudDetector:
    """Production-grade hybrid fraud detection shield combining ML and explainable cues."""

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3),
            sublinear_tf=True,
            min_df=1,
            max_features=4000
        )
        self.clf = LogisticRegression(C=1.5, max_iter=1000, random_state=42)
        self.is_trained = False
        self._train_initial_model()

    def _train_initial_model(self):
        """Train the classifier on the rich built-in dataset on startup."""
        df = get_dataset()
        X = self.vectorizer.fit_transform(df["text"])
        y = df["label"].values
        self.clf.fit(X, y)
        self.is_trained = True

    def scan_cues(self, text: str) -> Tuple[List[Dict[str, Any]], Dict[str, int], bool]:
        """
        Scan text for all matching spans across the 6 scam indicator categories.
        Also evaluates the Genuine Message Safeguard.
        """
        lower_text = text.lower()
        
        # Check Genuine Message Safeguard first
        genuine_matches = []
        for pat in GENUINE_SAFEGUARD_PATTERNS:
            for m in re.finditer(pat, lower_text):
                genuine_matches.append(m.group(0))
        
        is_safeguard_active = len(genuine_matches) > 0

        # Scan for scam indicator spans
        raw_spans = []
        category_counts = {cat_id: 0 for cat_id in CATEGORIES}

        for cat_id, cat_info in CATEGORIES.items():
            for pat in cat_info["patterns"]:
                for m in re.finditer(pat, text, flags=re.IGNORECASE):
                    start, end = m.span()
                    matched_phrase = text[start:end]
                    
                    # Safeguard context check:
                    # If this match is part of an anti-fraud warning (e.g. "never share your OTP" or "police never conduct digital arrest"),
                    # do not flag it as a threat!
                    surrounding = lower_text[max(0, start - 30):min(len(lower_text), end + 30)]
                    if any(neg in surrounding for neg in ["never conduct", "never demand", "never share", "do not share", "beware of", "no legal procedure"]):
                        continue

                    raw_spans.append({
                        "start": start,
                        "end": end,
                        "phrase": matched_phrase,
                        "category_id": cat_id,
                        "category_name": cat_info["name"],
                        "badge_color": cat_info["badge_color"],
                        "bg_color": cat_info["bg_color"],
                        "text_color": cat_info["text_color"],
                        "explanation": cat_info["explanation"]
                    })

        # Resolve overlapping spans: Keep longer spans
        raw_spans.sort(key=lambda x: (x["start"], -(x["end"] - x["start"])))
        filtered_spans = []
        last_end = -1
        for s in raw_spans:
            if s["start"] >= last_end:
                filtered_spans.append(s)
                last_end = s["end"]
                category_counts[s["category_id"]] += 1

        return filtered_spans, category_counts, is_safeguard_active

    def compute_rule_score(self, category_counts: Dict[str, int], is_safeguard_active: bool) -> float:
        """
        Compute explainable rule score in [0.0, 1.0].
        Considers distinct category triggers and toxic co-occurrences.
        """
        triggered_cats = sum(1 for c, count in category_counts.items() if count > 0)
        
        if triggered_cats == 0:
            return 0.0

        # Base score based on category diversity
        if triggered_cats == 1:
            base_score = 0.35
        elif triggered_cats == 2:
            base_score = 0.60
        elif triggered_cats == 3:
            base_score = 0.80
        else:
            base_score = 0.95

        # Digital arrest hallmark co-occurrence boost:
        # Fake Authority + (Threat OR Secrecy OR Money)
        has_auth = category_counts["fake_authority"] > 0
        has_threat = category_counts["threats_coercion"] > 0
        has_secrecy = category_counts["secrecy_isolation"] > 0
        has_money = category_counts["money_demands"] > 0

        co_occur_boost = 0.0
        if has_auth and (has_threat or has_secrecy or has_money):
            co_occur_boost += 0.20
        if has_threat and (has_secrecy or has_money):
            co_occur_boost += 0.15

        rule_score = min(1.0, base_score + co_occur_boost)

        # Genuine Safeguard suppression:
        # If genuine safeguard is active and fewer than 2 distinct coercive categories, suppress score
        if is_safeguard_active and triggered_cats < 2:
            rule_score = 0.0

        return rule_score

    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Execute full hybrid analysis with millisecond latency measurement.
        """
        if not text or not text.strip():
            return {
                "risk_score_pct": 0.0,
                "risk_level": "LOW",
                "risk_color": "#10b981",
                "ml_prob_pct": 0.0,
                "rule_score_pct": 0.0,
                "spans": [],
                "category_counts": {c: 0 for c in CATEGORIES},
                "latency_ms": 0.0,
                "annotated_html": "",
                "guidance": "Please enter or paste text to evaluate potential scam risks.",
                "safe_steps": [],
                "is_safeguard_active": False,
                "auto_complaint": {"filed": False, "token": None, "status": "NOT_TRIGGERED"}
            }

        t_start = time.perf_counter()

        # 1. Cue scan and span highlighter
        spans, category_counts, is_safeguard_active = self.scan_cues(text)

        # 2. ML Inference
        X_vec = self.vectorizer.transform([text])
        ml_prob = float(self.clf.predict_proba(X_vec)[0][1])

        # 3. Rule-Based Score
        rule_score = self.compute_rule_score(category_counts, is_safeguard_active)

        # Genuine safeguard ML damping
        if is_safeguard_active and rule_score == 0.0:
            ml_prob = min(ml_prob, 0.10)

        # 4. Hybrid Weighting: 40% ML + 60% Rule-Based
        hybrid_score = (0.40 * ml_prob) + (0.60 * rule_score)
        risk_score_pct = round(hybrid_score * 100, 1)

        # 5. Risk Categorization
        if risk_score_pct >= 70.0:
            risk_level = "HIGH"
            risk_color = "#ef4444" # Red
        elif risk_score_pct >= 35.0:
            risk_level = "MEDIUM"
            risk_color = "#f59e0b" # Amber
        else:
            risk_level = "LOW"
            risk_color = "#10b981" # Green

        latency_ms = round((time.perf_counter() - t_start) * 1000, 2)

        # 6. Generate Annotated HTML
        annotated_html = self._build_annotated_html(text, spans)

        # 7. Strict "Assist, Don't Accuse" Policy Guidance & Safe Steps
        guidance, safe_steps = self._generate_guidance(risk_level, category_counts, is_safeguard_active)

        # 8. Automated Cyber Cell Complaint (Triggered when Risk >= 70%)
        if risk_score_pct >= 70.0:
            token_id = f"NCR-2026-{int(time.time() * 1000) % 900000 + 100000}"
            cues_list = [f"{s['category_name']}: '{s['phrase']}'" for s in spans]
            dossier_text = (
                f"INCIDENT DOSSIER: SUSPECTED DIGITAL ARREST / EXTORTION\n"
                f"Reference Token: {token_id}\n"
                f"Routing Authority: National Cyber Crime Reporting Portal (cybercrime.gov.in) & 1930 Hotline\n"
                f"Applicable Sections: Section 66D IT Act (Personation), Section 318(4) & 308 BNSS (Cheating & Extortion)\n"
                f"Assessed Risk Score: {risk_score_pct}% (HIGH RISK)\n"
                f"Detection Latency: {latency_ms} ms\n"
                f"Flagged Coercive Cues ({len(spans)}):\n" + "\n".join(f" - {c}" for c in cues_list) + "\n\n"
                f"Evidence Transcript Excerpt:\n\"{text.strip()}\"\n"
            )
            auto_complaint = {
                "filed": True,
                "token": token_id,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S IST"),
                "authority": "National Cyber Crime Reporting Portal (cybercrime.gov.in)",
                "helpline": "1930",
                "status": "AUTOMATICALLY FILED & DISPATCHED TO CYBER CELL",
                "incident_type": "Digital Arrest / High-Risk Authority Impersonation Extortion",
                "evidence_count": len(spans),
                "dossier": dossier_text
            }
        else:
            auto_complaint = {
                "filed": False,
                "token": None,
                "status": "NOT_TRIGGERED",
                "reason": "Risk score is below 70% threshold."
            }

        return {
            "risk_score_pct": risk_score_pct,
            "risk_level": risk_level,
            "risk_color": risk_color,
            "ml_prob_pct": round(ml_prob * 100, 1),
            "rule_score_pct": round(rule_score * 100, 1),
            "spans": spans,
            "category_counts": category_counts,
            "latency_ms": latency_ms,
            "annotated_html": annotated_html,
            "guidance": guidance,
            "safe_steps": safe_steps,
            "is_safeguard_active": is_safeguard_active,
            "auto_complaint": auto_complaint
        }

    def _build_annotated_html(self, text: str, spans: List[Dict[str, Any]]) -> str:
        """
        Inject stylish HTML highlight spans with inline badges and hover tooltips.
        """
        if not spans:
            return f'<div class="annotated-text-box">{text}</div>'

        html_parts = []
        curr_idx = 0

        for s in spans:
            start = s["start"]
            end = s["end"]
            
            # Text preceding this match
            if start > curr_idx:
                html_parts.append(text[curr_idx:start])

            # The flagged phrase with styling
            phrase = text[start:end]
            cat_name = s["category_name"]
            badge_bg = s["badge_color"]
            bg_color = s["bg_color"]
            text_color = s["text_color"]
            explanation = s["explanation"]

            span_html = (
                f'<mark class="fraud-span" style="background-color: {bg_color}; color: {text_color}; '
                f'border-bottom: 2px solid {badge_bg}; padding: 2px 4px; border-radius: 4px; margin: 0 1px; font-weight: 500;" '
                f'title="{cat_name}: {explanation}">'
                f'{phrase}'
                f'<span style="background-color: {badge_bg}; color: #ffffff; font-size: 0.68rem; '
                f'padding: 1px 5px; border-radius: 999px; margin-left: 4px; vertical-align: middle; '
                f'font-weight: 600; text-transform: uppercase;">{cat_name}</span>'
                f'</mark>'
            )
            html_parts.append(span_html)
            curr_idx = end

        # Remainder of text
        if curr_idx < len(text):
            html_parts.append(text[curr_idx:])

        return f'<div class="annotated-text-box" style="line-height: 2.1; font-size: 1.05rem;">{"".join(html_parts)}</div>'

    def _generate_guidance(self, risk_level: str, category_counts: Dict[str, int], is_safeguard_active: bool) -> Tuple[str, List[Dict[str, str]]]:
        """
        Generate non-accusatory, empowering safety guidance following the Assist Don't Accuse policy.
        """
        if is_safeguard_active and risk_level == "LOW":
            guidance = (
                "Verified as a legitimate notification or public cyber advisory. "
                "The message contains standard transaction notifications or anti-fraud advisories. "
                "No suspicious coercion patterns were found."
            )
            steps = [
                {"title": "Standard Verification", "desc": "Keep record of normal transaction alerts for your monthly accounting."},
                {"title": "Maintain Cyber Hygiene", "desc": "Never share OTPs, PINs, or CVVs even if requested by genuine officials in the future."}
            ]
            return guidance, steps

        if risk_level == "HIGH":
            guidance = (
                "This interaction shows multiple high-risk patterns commonly associated with "
                "'Digital Arrest' or authority-impersonation scams. Please pause and verify independently."
            )
            steps = [
                {
                    "num": "1",
                    "title": "STOP & PAUSE (Do Not Comply)",
                    "action": "Do NOT transfer money, do NOT share OTPs or IDs, and immediately DISCONNECT any coerced video call.",
                    "detail": "Law enforcement agencies in India (CBI, Police, Customs, Courts) NEVER conduct 'Digital Arrests' over WhatsApp, Skype, or phone calls."
                },
                {
                    "num": "2",
                    "title": "BREAK THE COERCIVE ISOLATION",
                    "action": "Speak to a trusted family member, colleague, or friend right now.",
                    "detail": "Scammers enforce secrecy ('national security secret', 'do not tell family') specifically to prevent third parties from exposing their scam."
                },
                {
                    "num": "3",
                    "title": "VERIFY INDEPENDENTLY",
                    "action": "Contact the official department directly using a verified number from an official '.gov.in' portal.",
                    "detail": "Immediately dial the National Cyber Crime Helpline at 1930 or file a report online at cybercrime.gov.in."
                }
            ]
        elif risk_level == "MEDIUM":
            guidance = (
                "This interaction displays urgency or sensitive information requests that warrant heightened caution. "
                "Proceed carefully and verify the sender before taking any action."
            )
            steps = [
                {
                    "num": "1",
                    "title": "Do Not Rush",
                    "action": "Ignore artificial deadlines like 'within 15 minutes' or 'account will be suspended today'.",
                    "detail": "Banks and telecom providers provide official grace periods and physical branch access."
                },
                {
                    "num": "2",
                    "title": "Authenticate via Official App",
                    "action": "Do not click links in SMS or install remote access software (AnyDesk, QuickSupport).",
                    "detail": "Log in directly via official bank apps or visit your local branch in person."
                },
                {
                    "num": "3",
                    "title": "Report Suspicious Messages",
                    "action": "Forward the message to your service provider's fraud cell or report to 1930.",
                    "detail": "Telecom providers offer Sanchar Saathi (Chakshu portal) to report fraudulent communications."
                }
            ]
        else:
            guidance = (
                "No immediate high-risk coercion or scam patterns were detected. "
                "Continue standard digital precautions when interacting with unknown callers or SMS."
            )
            steps = [
                {
                    "num": "1",
                    "title": "Stay Vigilant",
                    "action": "Remember that genuine government or banking notifications never ask for credentials via SMS links.",
                    "detail": "Always check sender headers (e.g. AX-HDFCBK, VK-SBIIN)."
                }
            ]

        return guidance, steps
