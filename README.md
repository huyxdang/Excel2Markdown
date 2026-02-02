<h1 align="center">Excel to Markdown Convertner </h1>

<p align="center">
  <strong>Convert a complicated Excel (e.g., BRD) into LLM-friendly format in Markdown</strong>
</p>


---


### Overview
Note: Project for the Vietnam International Bank (VIB)

Sử dụng LLM để chuyển file Excel BRD thành dạng Markdown để giúp BA dễ đọc, hiểu, và giao việc cho devs dễ dàng hơn. 

Cho mỗi Excel file (37 sheets), quá trình chuyển đổi mất khoảng 17 phút (17m 12.6s)

Input = excel_file.xlsx ; Output = markdown_file.md

### Run 

Environment 
```
# Create env
python3 -m venv venv

# Activate env
source venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

Create an API key; Create file `.env` and enter your API key
```
ANTHROPIC_API_KEY = "your_key_here"
```

Running the workflow 
```
python main.py <excel_file.xlsx> --output-dir <output_path>

# Example
python mian.py data/BRD_input.xlsx --output-dir output
```