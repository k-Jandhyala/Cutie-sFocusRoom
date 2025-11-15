import google.generativeai as genai

genai.configure(api_key="AIzaSyB8YWnoZe-Ry3_eFp8yYlvRCgd6_aY1YoA")

model = genai.GenerativeModel("models/gemini-2.5-flash")

response = model.generate_content("Write a short paragraph about AI.")
print(response.text)


class QueryRequest(BaseModel):
    query: str

# Response model
class QueryResponse(BaseModel):
    response: str
    status: str

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        if not request.query:
            raise HTTPException(status_code=400, detail="No query provided")
        
        print(f"Received query: {request.query}")
        
        # Send query to Gemini
        response = model.generate_content(request.query)
        
        # Extract the text from the response
        gemini_output = response.text
        
        print(f"Gemini response: {gemini_output}")
        
        return QueryResponse(
            response=gemini_output,
            status="success"
        )
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))