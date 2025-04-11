import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import JsonResponse
import os
import math
from dotenv import load_dotenv

load_dotenv()


def chatbot_ui(request):
    return render(request, 'index.html')
GEMINI_API_URL=    os.getenv('GEMINI_API_URL')
GEMINI_APIKEY= os.getenv('GEMINI_APIKEY') 

@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            if not user_message:
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            payload = {
                "contents": [{"role": "user", "parts": [{"text": user_message}]}]
            }
            headers = {"Content-Type": "application/json"}

            response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_APIKEY}", json=payload, headers=headers)
            api_response = response.json()

            # Extract only the chatbot's reply
            bot_reply = api_response.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sorry, I couldn't generate a response.", )
            
            # Format the response for better readability
            formatted_reply = bot_reply.replace("**", "").replace("```", "\n") 
            

            return JsonResponse({"reply": formatted_reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

# def chatbot_response(request):
#     if request.method == "POST":
#         user_message = request.POST.get("message", "").strip()

#         if request.FILES.get("file"):
#             return JsonResponse({"response": "Sorry, I can't process images right now."})

#         bot_reply = generate_response(user_message)  
#         return JsonResponse({"response": bot_reply})

#     return JsonResponse({"response": "Invalid request."})



# def generate_response(user_input):
#     """Modify chatbot response to return structured JSON dynamically."""
#     user_input = user_input.lower()

#     if "prime numbers" in user_input:
#         response = {
#             "title": "Prime Number Finding Methods",
#             "methods": [
#                 {
#                     "name": "Basic Trial Division",
#                     "description": "Checks divisibility from 2 to n-1. Simple but slow.",
#                     "code": """def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True""",
#                     "example_usage": "print(is_prime(17))  # Output: True"
#                 },
#                 {
#                     "name": "Optimized Trial Division",
#                     "description": "Checks divisibility up to sqrt(n), reducing time complexity.",
#                     "code": """import math
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True""",
#                     "example_usage": "print(is_prime(97))  # Output: True"
#                 },
#                 {
#                     "name": "Sieve of Eratosthenes",
#                     "description": "Efficiently finds all primes up to a limit.",
#                     "code": """def sieve_of_eratosthenes(limit):
#     primes = [True] * (limit + 1)
#     p = 2
#     while p * p <= limit:
#         if primes[p]:
#             for i in range(p * p, limit + 1, p):
#                 primes[i] = False
#         p += 1
#     return [p for p in range(2, limit + 1) if primes[p]]""",
#                     "example_usage": "print(sieve_of_eratosthenes(50))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]"
#                 }
#             ]
#         }
#     else:
#         response = {"message": "I didn't understand your query. Please try again."}

#     return response

# def chatbot_view(request):
#     """Chatbot API endpoint"""
#     user_message = request.GET.get("message", "")
#     response_data = generate_response(user_message)
#     return JsonResponse(response_data)
