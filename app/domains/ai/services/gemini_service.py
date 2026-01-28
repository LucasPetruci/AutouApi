import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from app.exceptions.ai_exceptions import AIProcessingException, AIConfigurationException

load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise AIConfigurationException("GOOGLE_API_KEY not found in .env")
        
        genai.configure(api_key=api_key)
        
        model_name = os.getenv("AI_MODEL", "gemini-2.5-flash")
        self.model = genai.GenerativeModel(model_name)
        
        self.generation_config = {
            "temperature": 0.3,
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 1024,
        }
        
        self.language_map = {
            "pt-BR": "Portuguese (Brazil)",
            "en-US": "English (United States)",
            "es-ES": "Spanish (Spain)",
            "fr-FR": "French (France)",
            "de-DE": "German (Germany)"
        }
    
    def classify_email(self, content: str, language: str = "pt-BR") -> dict:
        prompt = self._build_prompt(content, language)
        
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            if not response.text:
                raise AIProcessingException("Gemini returned empty response")
            
            return self._parse_response(response.text)
            
        except Exception as e:
            raise AIProcessingException(f"Error processing with Gemini: {str(e)}")
    
    def _build_prompt(self, content: str, language: str) -> str:
        lang_name = self.language_map.get(language, "Portuguese (Brazil)")
        
        return f"""You are an assistant specialized in classifying corporate emails from the financial sector.

Analyze the email below and classify it into one of the following categories:

**PRODUCTIVE**: Emails that require action or specific response, such as:
- Technical support requests
- Status updates on open cases
- Questions about systems or processes
- Document or information requests
- Complaints or problems to be solved

**UNPRODUCTIVE**: Emails that don't require immediate action, such as:
- Greeting messages (birthdays, holidays, Christmas, etc.)
- Generic thanks
- Chains or spam
- Personal messages unrelated to work

After classifying, generate an appropriate, professional and polite automatic response in **{lang_name}**.

**Email to analyze:**
{content}

**IMPORTANT**: Respond ONLY with a valid JSON object. The "reasoning" field should be in English, but the "suggested_response" MUST be in {lang_name}. Use this exact format:

{{
    "category": "Productive" or "Unproductive",
    "confidence": number between 0 and 1,
    "suggested_response": "automatic response text in {lang_name}",
    "reasoning": "brief explanation in English"
}}"""
    
    def _parse_response(self, response: str) -> dict:
        try:
            response = response.strip()
            
            if response.startswith("```json"):
                response = response[7:]
            elif response.startswith("```"):
                response = response[3:]
            
            if response.endswith("```"):
                response = response[:-3]
            
            response = response.strip()
            
            data = json.loads(response)
            
            category = data.get("category", "Productive")
            confidence = float(data.get("confidence", 0.8))
            suggested_response = data.get("suggested_response", "")
            reasoning = data.get("reasoning", "")
            
            if category not in ["Productive", "Unproductive"]:
                category = "Productive"
            
            if not 0 <= confidence <= 1:
                confidence = 0.8
            
            if not suggested_response:
                raise AIProcessingException("Suggested response is empty")
            
            return {
                "category": category,
                "confidence": confidence,
                "suggested_response": suggested_response,
                "reasoning": reasoning
            }
            
        except json.JSONDecodeError as e:
            raise AIProcessingException(f"Error parsing JSON: {str(e)}")
        except Exception as e:
            raise AIProcessingException(f"Error processing response: {str(e)}")