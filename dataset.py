"""
Dataset for Digital Arrest & Real-Time Cyber Fraud Shield
Contains 60 rich, realistic labelled Indian examples:
- 30 Digital Arrest / Cyber Fraud transcripts, chat logs, and SMS (Label = 1)
- 30 Legitimate bank alerts, government advisories, OTPs, and delivery notifications (Label = 0)
"""

import pandas as pd

DATASET = [
    # ==========================================
    # 30 SCAM / DIGITAL ARREST EXAMPLES (Label = 1)
    # ==========================================
    {
        "id": 1,
        "text": "This is Inspector Vijay Rathore from Mumbai Cyber Crime Branch. A non-bailable warrant has been issued against you by Supreme Court in a money laundering case. You are placed under digital arrest right now. Do not disconnect the video call or tell anyone. You must transfer the money of 2,50,000 rupees to the RBI verification account immediately to clear your Aadhaar.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "CBI / Police Digital Arrest Call",
        "source": "Call Transcript"
    },
    {
        "id": 2,
        "text": "Customs Department Delhi Airport: We have intercepted an international FedEx parcel containing 140 grams of MDMA drugs and 5 fake passports booked under your Aadhaar number. Officer from CBI is handling your interrogation. You will be arrested today under NDPS Act. Stay on the video call, do not consult family or lawyer, and transfer 1,00,000 security deposit before 5 PM today.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Customs Parcel Drugs Threat",
        "source": "WhatsApp Call / Chat"
    },
    {
        "id": 3,
        "text": "TRAI Alert: Your mobile number has been found sending 1,200 illegal harassing messages. TRAI official has ordered immediate deactivation of all numbers linked to your Aadhaar within 15 minutes. Connect with Mumbai Cyber Crime cell officer immediately on WhatsApp video call to avoid police custody.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "TRAI Number Deactivation Threat",
        "source": "Automated IVR & Call"
    },
    {
        "id": 4,
        "text": "Attention: Enforcement Directorate notice. Serious financial fraud and hawala transactions detected in your Canara Bank account. You are implicated in a crime. Stay on the video call, do not consult family or lawyer, and share your bank statement and PAN card details right now for asset verification.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "ED Money Laundering Threat",
        "source": "Video Call Transcript"
    },
    {
        "id": 5,
        "text": "CBI Headquarters New Delhi: You are placed under digital arrest for 48 hours in connection with Naresh Goyal money laundering scam. Non-bailable warrant issued. Keep this confidential as it is a national security secret. RTGS/UPI transfer 3,00,000 refundable verification fee to RBI supervision account.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "CBI High-Profile Extortion",
        "source": "Call Transcript"
    },
    {
        "id": 6,
        "text": "Narcotics Control Bureau (NCB) Mumbai: A courier package from Taiwan addressed to your PAN card details contains contraband narcotics. Officer from CBI is taking over this case. Do not disconnect the line, do not tell anyone, and transfer the money immediately to avoid immediate raid at your house.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "NCB Contraband Parcel Scam",
        "source": "Skype Call Transcript"
    },
    {
        "id": 7,
        "text": "Dear Customer, your SBI YONO account has been blocked due to pending KYC verification. Update PAN and Aadhaar immediately within 15 minutes by clicking http://sbi-kyc-verify-portal.in to avoid permanent suspension and police complaint.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Bank KYC Suspension Threat",
        "source": "SMS Phishing"
    },
    {
        "id": 8,
        "text": "This is ACP Pradeep Sharma from cyber crime cell. Your Aadhaar card is compromised and registered in 16 illicit bank accounts across India. You are facing non-bailable warrant. Share OTP received on your mobile and net banking password to authenticate your innocence immediately.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Cyber Cell Aadhaar Compromise",
        "source": "Phone Call Transcript"
    },
    {
        "id": 9,
        "text": "High Court of Delhi digital summon: Contempt of court and financial terrorism charges framed against you. You are under digital arrest. Remain in a closed room alone on this video call, do not consult anyone, and deposit 1,50,000 rupees security deposit to court registrar account immediately.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "High Court Digital Warrant Scam",
        "source": "WhatsApp Video Call"
    },
    {
        "id": 10,
        "text": "Urgent Electricity Bill Notice: Dear consumer, your power supply will be disconnected tonight at 9:30 PM due to unpaid bill of previous month. Immediately call our power officer on 9876543210 and share screen share via AnyDesk to verify payment receipt right now.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Electricity Disconnection Scam",
        "source": "SMS / Chat"
    },
    {
        "id": 11,
        "text": "National Investigation Agency (NIA) summons: Terror funding link found originating from your mobile IP address. Supreme Court warrant issued. You are placed under digital arrest right now. Do not tell anyone or inform local police. Transfer total bank balance to RBI safe custody account within 30 minutes.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "NIA Terror Link Coercion",
        "source": "Call Transcript"
    },
    {
        "id": 12,
        "text": "Telecom Regulatory Authority of India: All SIM cards registered against your Aadhaar will be terminated within 2 hours due to cyber harassment. To cancel arrest warrant, press 9 to connect with CBI officer on call immediately and submit your security deposit.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "TRAI Interactive Voice Scam",
        "source": "IVR Transfer"
    },
    {
        "id": 13,
        "text": "Customs Department Mumbai Seaport: Illegal consignment of gold bars and synthetic drugs found with your passport copy. You will be arrested today unless you cooperate. Stay on the video call continuously, do not disconnect, and send 75,000 rupees refundable verification fee to RBI supervision account.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Customs Gold & Narcotics Scam",
        "source": "WhatsApp Call"
    },
    {
        "id": 14,
        "text": "Cyber Police Headquarters: We have caught a child pornography ring and your IP address is implicated in a crime. Non-bailable warrant is signed by magistrate. Keep this confidential, do not tell anyone in your house, and transfer 50,000 penalty immediately to settle the case without public arrest.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Cyber Cell Defamation Extortion",
        "source": "Call Transcript"
    },
    {
        "id": 15,
        "text": "Income Tax Department Emergency Notice: Tax evasion and money laundering case detected for AY 2025-26. Penalty of Rs 85,000 levied. Pay within 15 minutes via UPI link http://itax-instant-penalty.link or face immediate arrest by Enforcement Directorate squad.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Income Tax ED Raid Threat",
        "source": "SMS / WhatsApp"
    },
    {
        "id": 16,
        "text": "You are speaking to Special Task Force Officer Rajesh Kumar. A student suicide case is traced to your WhatsApp chats. You will be taken into police custody right now. Stay in your room, do not tell family or lawyer, keep this confidential, and share your net banking password and OTP to clear your name.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Police STF False Accusation",
        "source": "Phone Call Transcript"
    },
    {
        "id": 17,
        "text": "DHL Express Warning: Parcel tracking DHL-98218-IN containing 16 forged credit cards and illegal foreign currency seized at customs. Arrest warrant issued against recipient. You must connect on Skype with Narcotics Control Bureau officer right now. Do not hang up or you will be jailed.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "DHL Courier Customs Seizure",
        "source": "Voice Call / SMS"
    },
    {
        "id": 18,
        "text": "HDFC Bank Alert: Suspicious transaction of 89,000 rupees attempted on your debit card. To freeze your bank accounts and prevent complete loss, share OTP received right now with security officer on call. Failure to cooperate within 5 minutes will result in total loss.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Bank Fraud Impersonation",
        "source": "Vishing Call"
    },
    {
        "id": 19,
        "text": "Supreme Court of India e-Committee: Urgent digital arrest notice. You are summoned for hearing via video conference in money laundering case. Do not leave your seat, keep camera turned on, do not consult anyone. Transfer 2,00,000 security deposit to the court registry account before 5 PM today.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Supreme Court Video Hearing Scam",
        "source": "Video Call Transcript"
    },
    {
        "id": 20,
        "text": "Crime Branch Anti-Extortion Cell: Your son is in police custody for a hit-and-run accident causing fatal injury. If you want him released without non-bailable warrant and FIR, transfer 1,50,000 rupees via RTGS/UPI transfer immediately within 15 minutes. Do not call anyone else or he will be jailed.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Family Emergency / Arrest Scam",
        "source": "Emergency Call Scam"
    },
    {
        "id": 21,
        "text": "RBI Verification Officer: In accordance with Central Vigilance Commission guidelines, all citizens must verify their bank accounts. Transfer the money in your savings account to RBI supervision account for 24 hours audit. Failure to do so will result in frozen bank accounts and police arrest.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "RBI Verification Scam",
        "source": "Call Transcript"
    },
    {
        "id": 22,
        "text": "Interpol New Delhi Office: Red corner notice alert linked to your passport and Aadhaar. Stay on the video call, do not disconnect, keep this confidential as it involves national security secret. Pay 5,00,000 refundable verification fee to avoid detention at international airports.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Interpol Red Notice Scam",
        "source": "Skype Video Call"
    },
    {
        "id": 23,
        "text": "Your credit card reward points worth Rs 9,850 are expiring today. Claim cash refund to your bank account immediately by sharing CVV, card expiry date, and login OTP on http://rewards-hdfc-claim.xyz within 10 minutes.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Reward Points Credential Phishing",
        "source": "SMS Phishing"
    },
    {
        "id": 24,
        "text": "CBI Officer Anand Roy: We have seized illegal firearms shipped under your name. You are under digital arrest. Do not consult family or lawyer, do not disconnect the call. Transfer 3,50,000 security deposit to RBI verification account right now to prove you are a victim not a conspirator.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "CBI Arms Trafficking Scam",
        "source": "Video Call Transcript"
    },
    {
        "id": 25,
        "text": "Mumbai Police Cyber Cell: Your Aadhaar was used to rent a server used in dark web extortion. Non-bailable warrant issued. Stay on this WhatsApp call, share screen share, and disclose all bank balances immediately to prevent immediate police raid.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Dark Web Server Impersonation",
        "source": "WhatsApp Call"
    },
    {
        "id": 26,
        "text": "Postal Department India Post: Parcel IND-88190 cannot be delivered due to incomplete house address. Update your address and pay 25 rupees redelivery fee within 15 minutes at http://indiapost-update.top or your parcel will be handed to Customs Department for confiscation.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "India Post Smishing",
        "source": "SMS Phishing"
    },
    {
        "id": 27,
        "text": "Cyber Crime Department Bangalore: A digital arrest warrant has been approved against you for financial fraud. Keep this confidential and do not tell anyone. Stay on the video call and transfer the money of 1,20,000 to the court clearance account right now.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Cyber Crime Warrant Threat",
        "source": "Call Transcript"
    },
    {
        "id": 28,
        "text": "Enforcement Directorate New Delhi: We have sealed your company bank accounts under Prevention of Money Laundering Act. To prevent immediate public arrest of directors, submit security deposit of 4,00,000 to government designated escrow account before 5 PM today.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "ED Company Raids Threat",
        "source": "Formal Threat Letter & Call"
    },
    {
        "id": 29,
        "text": "TRAI & Mumbai Police: Your Aadhaar has been blacklisted across all Indian telecom operators. You are implicated in a crime. You will be arrested today within 2 hours. Do not consult anyone, remain isolated in your room on video call, and transfer 80,000 refundable verification fee right now.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "Telecom Blacklist Coercion",
        "source": "WhatsApp Video Call"
    },
    {
        "id": 30,
        "text": "High Court Bailiff & Cyber Cell: Arrested today order signed. To avoid public dishonor and police custody, stay on video call, share PAN card details and bank statement, and RTGS/UPI transfer 1,75,000 security deposit immediately.",
        "label": 1,
        "label_text": "Scam / Coercion",
        "scenario": "High Court Bailiff Coercion",
        "source": "Call Transcript"
    },

    # ==========================================
    # 30 LEGITIMATE / SAFE EXAMPLES (Label = 0)
    # ==========================================
    {
        "id": 31,
        "text": "Dear Customer, INR 4,500.00 debited from A/c XX4821 on 22-Oct-2026 10:15 AM via UPI to SWIGGY. Ref no 62940182. If not done by you, forward this SMS to 9223008333 or call 1800-258-4455. - HDFC Bank",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Bank Debit Alert",
        "source": "Bank Transaction SMS"
    },
    {
        "id": 32,
        "text": "SBI OTP: 618302 is your secret one-time password for transaction of INR 1,200.00 at AMAZON. Valid for 10 minutes. NEVER SHARE YOUR OTP, CVV, or passwords with anyone, including bank officials or police.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Bank OTP with Anti-Fraud Warning",
        "source": "Bank OTP SMS"
    },
    {
        "id": 33,
        "text": "Delhi Police Cyber Cell Advisory: Citizens are warned that genuine police and government agencies NEVER conduct 'digital arrest' or demand money transfers over WhatsApp or Skype. Report any cyber extortion at cybercrime.gov.in or helpline 1930.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Police Cyber Awareness Advisory",
        "source": "Government Public Service SMS"
    },
    {
        "id": 34,
        "text": "TRAI Consumer Advisory: TRAI never calls consumers regarding mobile disconnection or verification. Do not entertain calls threatening number deactivation. File complaints with your telecom service provider or on the Sanchar Saathi portal.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "TRAI Anti-Scam Public Alert",
        "source": "Telecom Regulatory Advisory"
    },
    {
        "id": 35,
        "text": "Dear Citizen, your periodic re-KYC for Axis Bank Account ending 7731 is due. Please visit your home branch with your original PAN and Aadhaar or complete video KYC through the official Axis Mobile application. We never ask for confidential pins.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Routine Bank KYC Reminder",
        "source": "Bank Official Email/SMS"
    },
    {
        "id": 36,
        "text": "Income Tax Department: Refund of INR 8,420 for Assessment Year 2026-27 has been credited to your validated bank account ending in 3319. To check refund status, please visit the official portal at incometax.gov.in.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Income Tax Official Refund Notification",
        "source": "Government ITD Notification"
    },
    {
        "id": 37,
        "text": "Ekart Logistics: Your Flipkart package with tracking ID FMPC10928472 is out for delivery. Agent Suresh will deliver between 2 PM and 5 PM. Provide delivery verification code 8391 to the agent only upon receiving the package.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "E-commerce Delivery Update",
        "source": "Delivery SMS"
    },
    {
        "id": 38,
        "text": "ICICI Bank Alert: Your Credit Card ending 9012 monthly statement is generated. Total Amount Due: INR 15,340.00. Minimum Due: INR 1,200.00. Payment Due Date: 05-Nov-2026. Pay safely through iMobile Pay app or Net Banking.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Credit Card Monthly Statement",
        "source": "Bank Official SMS"
    },
    {
        "id": 39,
        "text": "Cyber Dost (MHA Initiative): Beware of scam calls claiming parcels with illegal drugs or fake CBI/ED warrants. Genuine police will never demand money transfers or ask you to stay on video calls. Dial 1930 to report fraud.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Ministry of Home Affairs Cyber Alert",
        "source": "MHA Public Broadcast"
    },
    {
        "id": 40,
        "text": "Indian Railways IRCTC: PNR 284-9182746 Train 12951 Mumbai Rajdhani. Confirmed: Coach B3, Berth 42 (Side Lower). Date of Journey: 25-Oct-2026. Have a safe journey. IRCTC never sends APK files.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Train Ticket Booking Confirmation",
        "source": "IRCTC Official SMS"
    },
    {
        "id": 41,
        "text": "Dear Customer, INR 25,000.00 deposited into A/c XX8192 on 22-Oct-2026 by NEFT from INFOSYS TECHNOLOGIES. Available Balance: INR 68,410.50. - State Bank of India",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Salary Deposit Credit SMS",
        "source": "Bank Credit Alert"
    },
    {
        "id": 42,
        "text": "EPFO Notification: Universal Account Number (UAN) 100928374619 mobile number updated successfully. If not requested by you, contact epfigms.gov.in. EPFO officials never call requesting bank transfer or OTP.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "EPFO Profile Security Notification",
        "source": "Government Portal Alert"
    },
    {
        "id": 43,
        "text": "Tata Power Consumer Notice: Bill of INR 1,840 for CA 900182736 has been generated. Due date is 02-Nov-2026. Pay securely on tatapower.com/billpay or through official UPI apps. Ignore calls asking to download third-party quick support apps.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Utility Electricity Bill Notice",
        "source": "Utility Official SMS"
    },
    {
        "id": 44,
        "text": "IndiGo Airlines: Web check-in for flight 6E-204 from Delhi to Bengaluru on 24-Oct is now open. Confirm your seat on goindigo.in or IndiGo App. Carry government-issued photo ID to the airport.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Airline Web Check-in Notice",
        "source": "Airline Communication"
    },
    {
        "id": 45,
        "text": "Reserve Bank of India Public Notice: Beware of fictitious offers of large sums from overseas, lottery prizes, or demands for tax clearance fees. RBI does not hold accounts for individuals. Do not send money.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "RBI Official Caution Notice",
        "source": "RBI Public Awareness"
    },
    {
        "id": 46,
        "text": "Dear Customer, your Kotak Mahindra Bank debit card ending 4019 has been used for an international ATM withdrawal of USD 100. If unauthorized, immediately lock your card on the Kotak App or SMS BLOCK to 5676788.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Fraud Prevention Real-Time Alert",
        "source": "Bank Security SMS"
    },
    {
        "id": 47,
        "text": "Amazon India: Your order #402-9812734-11823 has been shipped and will arrive tomorrow by 8 PM. Track your package on amazon.in. Never share your password or OTP over the phone.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "E-Commerce Shipping Notification",
        "source": "Amazon Official SMS"
    },
    {
        "id": 48,
        "text": "UIDAI Aadhaar Security Alert: OTP generated to verify Aadhaar authentication for e-Sign. Valid for 10 minutes. If you did not initiate this request, lock your biometrics using mAadhaar app or visit uidai.gov.in.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "UIDAI Biometric / OTP Notice",
        "source": "UIDAI Official Alert"
    },
    {
        "id": 49,
        "text": "Mumbai Police Advisory: There is no legal procedure called 'Digital Arrest' under Indian criminal law (BNSS / IPC). Police officers will never examine suspects over video call. If threatened, call 100 or 1930 immediately.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "State Police Legal Clarification",
        "source": "Police Official Advisory"
    },
    {
        "id": 50,
        "text": "Zerodha Alert: Funds transfer of INR 50,000 credited to your trading account 29381. Funds will be available for equity trading tomorrow. Zerodha employees will never ask for your 2FA TOTP or Kite password.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Brokerage Fund Confirmation",
        "source": "Stock Broker Notice"
    },
    {
        "id": 51,
        "text": "Swiggy Order Confirmed: Your dinner from Biryani By Kilo is being prepared! Estimated delivery time: 35 minutes. Order total INR 640 paid via UPI. Track your delivery partner on the Swiggy app.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Food Delivery Confirmation",
        "source": "App Transaction Update"
    },
    {
        "id": 52,
        "text": "Airtel Thanks: Your recharge of INR 349 is successful. 2GB/day + Unlimited Calls for 28 days active. Check balance anytime on Airtel Thanks App. Airtel never calls asking you to dial codes to prevent SIM blocking.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Telecom Prepaid Recharge Notice",
        "source": "Telecom Provider Alert"
    },
    {
        "id": 53,
        "text": "Bank of Baroda: Dear Customer, 10,000 reward points credited to your account for festival shopping. Redeem directly on bobcard.co.in. No phone call or personal PIN sharing is required to claim points.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Bank Loyalty Points Official Update",
        "source": "Official Bank Notification"
    },
    {
        "id": 54,
        "text": "Passport Seva Portal: Appointment for Passport Renewal confirmed at PSK Andheri West on 28-Oct-2026 at 11:30 AM. Application ARN: 26-1029384721. Bring original documents. MEA never demands cash or video verification.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Passport Seva Appointment",
        "source": "Passport Seva SMS"
    },
    {
        "id": 55,
        "text": "Jio Fiber: Your high-speed broadband plan renewal is due in 3 days on 25-Oct. Pay INR 1,179 securely via MyJio app or visit jio.com to ensure uninterrupted 150 Mbps connection.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Internet Service Billing Reminder",
        "source": "Broadband Provider Alert"
    },
    {
        "id": 56,
        "text": "National Payments Corporation of India (NPCI) Advisory: UPI PIN is used ONLY to deduct money from your account, NEVER to receive money. Do not enter PIN when receiving cashback or refunds from strangers.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "NPCI UPI Safety Guidance",
        "source": "NPCI Consumer Advisory"
    },
    {
        "id": 57,
        "text": "Apollo Pharmacy: Your prescription medicines order #AP-88291 has been packed and handed to delivery partner. Expected delivery by 4 PM. Bill amount: INR 840 paid online. Thank you for choosing Apollo.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Pharmacy Order Delivery",
        "source": "Healthcare Order Alert"
    },
    {
        "id": 58,
        "text": "Delhi High Court Cause List Notification: Item No. 14 in Court Room 3 (Civil Writ Petition 4810/2026) is scheduled for virtual hearing on 26-Oct at 10:30 AM. VC link published on official website delhihighcourt.nic.in.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Genuine Court Hearing Cause List",
        "source": "High Court Official Listing"
    },
    {
        "id": 59,
        "text": "Uber India: Your ride with Driver Ramesh (Maruti Dzire DL 1Z A9021) is arriving in 4 minutes. Share PIN 4821 only when you board the cab. Trip fare estimated: INR 210. Stay safe.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "Cab Ride PIN Confirmation",
        "source": "Mobility App SMS"
    },
    {
        "id": 60,
        "text": "Cert-In Cyber Advisory: Vulnerability advisory issued for Android OS versions 12 and below. Users are advised to install monthly security patches from device settings. Report incidents to incident@cert-in.org.in.",
        "label": 0,
        "label_text": "Legitimate",
        "scenario": "CERT-In National Vulnerability Advisory",
        "source": "CERT-In Cyber Advisory"
    }
]

def get_dataset():
    """Return the labelled dataset as a pandas DataFrame."""
    return pd.DataFrame(DATASET)

# Preset samples for Tab 1 demo selector
PRESET_SAMPLES = {
    "1. Classic CBI Digital Arrest Call Transcript (High Risk)": (
        "This is Inspector Vijay Rathore from Mumbai Cyber Crime Branch. "
        "A non-bailable warrant has been issued against you by Supreme Court in a money laundering case. "
        "You are placed under digital arrest right now. Do not disconnect the video call or tell anyone. "
        "You must transfer the money of 2,50,000 rupees to the RBI verification account immediately "
        "to clear your Aadhaar and settle the case before police custody."
    ),
    "2. Customs / Parcel Drugs Threat Chat (High Risk)": (
        "Customs Department Delhi Airport: We have intercepted an international FedEx parcel "
        "containing 140 grams of MDMA drugs and 5 fake passports booked under your Aadhaar number. "
        "Officer from CBI is taking over. You will be arrested today under NDPS Act. "
        "Stay on the video call, do not consult family or lawyer, and transfer 1,00,000 security deposit "
        "to the government clearance account before 5 PM today."
    ),
    "3. Urgent Bank KYC Suspension SMS (Medium Risk)": (
        "Dear Customer, your SBI YONO account KYC verification is pending. "
        "Update your PAN card details within 24 hours at http://sbi-kyc-portal.net "
        "to avoid service interruption."
    ),
    "4. Genuine Bank OTP & Fraud Warning SMS (Low Risk - Legitimate)": (
        "SBI OTP: 618302 is your secret one-time password for transaction of INR 1,200.00 at AMAZON. "
        "Valid for 10 minutes. NEVER SHARE YOUR OTP, CVV, or passwords with anyone, "
        "including bank officials or police. Report fraud at 1930."
    ),
    "5. Genuine Government/Police Cyber Awareness Alert (Low Risk - Legitimate)": (
        "Delhi Police Cyber Cell Advisory: Citizens are warned that genuine police and government agencies "
        "NEVER conduct 'digital arrest' or demand money transfers over WhatsApp or Skype. "
        "Report any cyber extortion at cybercrime.gov.in or helpline 1930."
    ),
    "6. Custom Input (Type or Paste Your Own Text)": ""
}
