import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")


def check_openai():
    """Checks for available OpenAI models"""
    if not OPENAI_KEY:
        print("[-] OpenAI: Skipped (No API Key found)")
        return

    print(f"\n[+] Checking OpenAI models...")
    try:
        from openai import OpenAI

        client = OpenAI(api_key=OPENAI_KEY)

        models = client.models.list()
        gpt_models = [m.id for m in models.data if "gpt" in m.id]
        gpt_models.sort()

        print(f"    Found {len(gpt_models)} GPT models:")
        for model_id in gpt_models:
            print(f"    - {model_id}")

    except Exception as e:
        print(f"    ! Error checking OpenAI: {e}")


def check_google():
    """Checks for available Google models using the NEW SDK (v1.0+)"""
    if not GOOGLE_KEY:
        print("[-] Google: Skipped (No API Key found)")
        return

    print(f"\n[+] Checking Google Gemini models...")
    try:
        from google import genai

        client = genai.Client(api_key=GOOGLE_KEY)

        print("    Found the following content generation models:")

        # Iterate over models using the new SDK structure
        for model in client.models.list():
            # ATTRIBUTE FIX: Use 'supported_actions' instead of 'supported_generation_methods'
            # We explicitly check if this attribute exists to prevent future errors
            actions = getattr(model, "supported_actions", []) or []

            if "generateContent" in actions:
                # 'model.name' usually comes as 'models/gemini-1.5-flash'
                display_name = model.name.replace("models/", "")
                print(f"    - {display_name}")

    except Exception as e:
        print(f"    ! Error checking Google: {e}")
        # Debug helper: if it fails again, this prints what attributes actually exist
        # import inspect
        # print(dir(e))


if __name__ == "__main__":
    print("--- MODEL CHECKER (OpenAI & Google) ---")
    check_openai()
    check_google()
    print("\n--- CHECK COMPLETE ---")
