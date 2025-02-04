import pandas as pd
from fpdf import FPDF

# Function to load and analyze data
def load_and_analyze_data(file_path):
    df = pd.read_csv(file_path)  # Load the dataset
    summary = df.describe().round(2)  # Summary statistics
    correlation = df.corr().round(2)  # Correlation matrix
    return df, summary, correlation

# Function to generate PDF report
def generate_pdf_report(df, summary, correlation, output_file):
    pdf = FPDF()  # Initialize PDF
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # Add dataset overview
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Dataset Overview", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Number of Rows: {df.shape[0]}", ln=True)
    pdf.cell(200, 10, txt=f"Number of Columns: {df.shape[1]}", ln=True)
    pdf.ln(10)

    # Add summary statistics
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Summary Statistics", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(200, 10, txt=summary.to_string(), align="L")
    pdf.ln(10)

    # Add correlation matrix
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Correlation Matrix", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(200, 10, txt=correlation.to_string(), align="L")
    pdf.ln(10)

    # Save the PDF
    pdf.output(output_file)

# Main function
def main():
    input_file = "data.csv"  # Replace with your dataset file
    output_file = "report.pdf"  # Output PDF file

    # Load and analyze data
    df, summary, correlation = load_and_analyze_data(input_file)

    # Generate PDF report
    generate_pdf_report(df, summary, correlation, output_file)
    print(f"Report generated successfully: {output_file}")

# Run the script
if __name__ == "__main__":
    main()