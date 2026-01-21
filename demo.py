#!/usr/bin/env python3
"""
ClinicalNote AI Assistant - Interactive Demo
MedGemma Impact Challenge Submission

This demo shows the core functionality of the clinical documentation assistant.
"""

class SOAPNote:
    """Structured SOAP note format"""
    
    def __init__(self, subjective, objective, assessment, plan, icd10_codes):
        self.subjective = subjective
        self.objective = objective
        self.assessment = assessment
        self.plan = plan
        self.icd10_codes = icd10_codes
    
    def to_formatted_text(self):
        """Format as readable clinical note"""
        note = "\n" + "="*60 + "\n"
        note += "CLINICAL NOTE (For Physician Review)\n"
        note += "="*60 + "\n\n"
        note += "SUBJECTIVE:\n"
        note += self.subjective + "\n\n"
        note += "OBJECTIVE:\n"
        note += self.objective + "\n\n"
        note += "ASSESSMENT:\n"
        note += self.assessment + "\n\n"
        note += "PLAN:\n"
        note += self.plan + "\n\n"
        note += "ICD-10 CODES:\n"
        note += ', '.join(self.icd10_codes) + "\n"
        note += "="*60 + "\n"
        note += "NOTE: Physician review required before finalization.\n"
        note += "="*60 + "\n"
        return note


def generate_soap_note_demo(conversation):
    """
    Demo function - simulates SOAP note generation.
    
    In production, this would call the fine-tuned MedGemma model.
    For demo purposes, uses keyword-based generation.
    """
    
    conversation_lower = conversation.lower()
    
    if "sore throat" in conversation_lower and "strep" in conversation_lower:
        return SOAPNote(
            subjective="Chief Complaint: Sore throat x 3 days\n\nPatient reports difficulty swallowing and throat pain for 3 days. Fever documented at 101°F yesterday. Patient also notes mild cough.",
            objective="Vital Signs: Temperature 100.2°F\n\nPhysical Examination:\n- HEENT: Throat erythematous with white exudates on tonsils\n- Lymphatic: Bilateral cervical lymphadenopathy\n- Respiratory: Lungs clear\n\nDiagnostic Testing:\n- Rapid strep test: POSITIVE",
            assessment="Acute streptococcal pharyngitis (physician diagnosis based on clinical presentation and positive rapid strep test)",
            plan="TREATMENT PLAN (as prescribed by physician):\n\n1. Amoxicillin 500mg PO TID x 10 days\n2. Ibuprofen 400mg PO Q6H PRN for pain/fever\n3. Patient education: Complete antibiotics, increase fluids, rest\n4. Return if symptoms persist >3 days or worsen",
            icd10_codes=["J02.0 - Streptococcal pharyngitis", "R50.9 - Fever, unspecified"]
        )
    else:
        return SOAPNote(
            subjective="Patient presents with chief complaint as documented in encounter.",
            objective="Physical examination findings as documented by physician.",
            assessment="Clinical assessment as determined by physician.",
            plan="Treatment plan as prescribed by physician.",
            icd10_codes=["Z00.00 - General examination"]
        )


def run_demo():
    """Run interactive demo"""
    
    print("\n" + "="*70)
    print("CLINICALNOTE AI ASSISTANT - DEMO")
    print("MedGemma Impact Challenge Submission")
    print("="*70)
    print("\nThis demo shows how the system generates structured SOAP notes")
    print("from physician-patient conversations.\n")
    print("IMPORTANT: This is a DOCUMENTATION tool. It documents what the")
    print("physician said/did - it does NOT make clinical decisions.\n")
    print("="*70)
    
    # Sample conversation
    sample_conversation = """Doctor: Good morning, what brings you in today?
Patient: I've had a terrible sore throat for about 3 days now. It hurts to swallow.
Doctor: I see. Any fever?
Patient: Yes, I had a fever yesterday. It was about 101°F.
Doctor: Any other symptoms? Cough, runny nose?
Patient: A little bit of a cough, but mostly just the sore throat.
Doctor: Let me take a look. Your throat is quite red and inflamed. I can see some white patches on your tonsils. Your lymph nodes are also swollen. Temperature today is 100.2°F. Lung sounds are clear.
Patient: What do you think it is?
Doctor: This looks like strep throat. I'm going to do a rapid strep test to confirm. The test is positive for strep.
Patient: What should I do?
Doctor: I'll prescribe you amoxicillin 500mg three times a day for 10 days. Take all of it even if you feel better. You should start feeling better in 24-48 hours. Rest, drink plenty of fluids, and you can take ibuprofen for the pain and fever. If you're not better in 3 days or get worse, call me."""
    
    print("\nSAMPLE CLINICAL CONVERSATION:")
    print("-" * 70)
    print(sample_conversation)
    print("-" * 70)
    
    print("\nGenerating SOAP note...")
    print("(In production, this uses fine-tuned MedGemma)")
    
    # Generate note
    soap_note = generate_soap_note_demo(sample_conversation)
    
    # Display
    print(soap_note.to_formatted_text())
    
    print("\n" + "="*70)
    print("KEY POINTS:")
    print("- AI documented what physician said/did")
    print("- AI did NOT make clinical decisions")
    print("- Physician review required before finalization")
    print("="*70)
    print("\n✅ Demo completed!\n")


if __name__ == "__main__":
    run_demo()
