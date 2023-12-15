from models.search import SearchRequestParam
from setting import API_KEY

import google.generativeai as genai

def generate_by_gemini_logic(param: SearchRequestParam) -> str:
  GOOGLE_API_KEY = API_KEY
  genai.configure(api_key=GOOGLE_API_KEY)

  model = genai.GenerativeModel('gemini-pro')

  prompt = f'''
The following is the output result of the git diff command.
Please generate 5 candidate commit messages for committing this change to Git in the following JSONformat.

Sample Format: 
{{"messages": [
  "Candidate 1",
  "Candidate 2",
  "Candidate 3",
  "Candidate 4",
  "Candidate 5"
]}}

result of the git diff command: ```
{param.diff}
```
'''
  
  response = model.generate_content(prompt)

  json_str = response.text.replace('```', '')
  json_str = json_str.replace('JSON\n', '')

  print(json_str)
  return json_str