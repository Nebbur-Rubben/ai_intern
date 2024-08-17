import openai
import os
import PyPDF2

# Initialize the OpenAI client with your specific API key
client = openai.OpenAI(api_key="sk-proj-9666MYtxPRNdYpNIUWPbT3BlbkFJ7meSrLDHcGelTMJRbjBs")  # Replace with your actual API key

def read_pdf(file_path):
    """Reads a PDF file and returns the text content of each page as a list."""
    text_contents = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text_contents.append(page.extract_text())
    return text_contents

def send_to_openai(text_content):
    """Sends the given text content to the OpenAI GPT-4 model and returns the response."""
    try:
        # Modify the prompt to act according to the new content requirements
        prompt = f"""
        Create detailed explanations and clarifications about STM32 Discovery Kits based on the text provided. Specifically, focus on:
        - Pin configurations
        - Pin functions
        - Connections and interactions between pins
        - Examples of usage for specific pins

        TEXT CONTENT:
        {text_content}

        STRICTLY FOLLOW THIS SYNTAX FOR EACH ENTRY, DO NOT ADD ANYTHING ELSE to the SYNTAX:
        {{
            "messages": [
                {{"role": "system", "content": "You are an expert in STM32 Discovery Kits and electronics."}},
                {{"role": "user", "content": "Provide detailed explanations about STM32 Discovery Kit pins, including their configurations, functions, and usage examples based on the provided text."}},
                {{"role": "assistant", "content": "Detailed and expanded response regarding the pins, configurations, and usage examples."}}
            ]
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "You are an expert in STM32 Discovery Kits and electronics, creating fine-tuning data for educational and technical purposes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.7,
            top_p=1
        )

        response_text = response.choices[0].message.content

        return response_text

    except Exception as e:
        print("An error occurred:", e)
        return None

def process_pdf(file_path, output_dir):
    """Processes the PDF and saves the responses in a single output file within the output directory."""
    text_contents = read_pdf(file_path)
    all_responses = ""

    for page_num, text_content in enumerate(text_contents):
        print(f"Processing page {page_num + 1}/{len(text_contents)} of {os.path.basename(file_path)}")
        response_text = send_to_openai(text_content)
        if response_text:
            all_responses += response_text + "\n\n"

    output_file_path = os.path.join(output_dir, os.path.basename(file_path).replace('.pdf', '_fine_tuning.json'))
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(all_responses)
    print(f"Finished processing {os.path.basename(file_path)}. Output saved to {output_file_path}")

def process_directory(directory_path):
    """Processes all PDF files within a directory and saves the fine-tuning data in a new folder."""
    output_dir = os.path.join(directory_path, 'processed_fine_tuning')
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(directory_path, file_name)
            process_pdf(file_path, output_dir)

if __name__ == "__main__":
    # Change the directory path to the folder where you hold the PDF
    directory_path = r"D:\STM32 Discovery Kits_Yang Xu\datasheet"  # Specify the path to the PDF file
    process_directory(directory_path)
