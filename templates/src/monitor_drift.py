import os
import pandas as pd
import joblib
import boto3
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset

# Simular dados
ref_df = pd.read_csv("data/sample_ref.csv")
prod_df = pd.read_csv("data/sample_prod.csv")

# Gerar relatório
report = Report(metrics=[DataDriftPreset(), TargetDriftPreset()])
report.run(reference_data=ref_df, current_data=prod_df)

# Salvar local
json_path = "monitoring/drift_report.json"
report.save_json(json_path)

print(f"Relatório Evidently salvo localmente em {json_path}")

# Upload para S3
S3_BUCKET = os.getenv("S3_BUCKET", "cd4ml-monitoring")
S3_KEY = "drift_reports/drift_report.json"

s3 = boto3.client("s3")
s3.upload_file(json_path, S3_BUCKET, S3_KEY)
print(f"Relatório enviado para S3: s3://{S3_BUCKET}/{S3_KEY}")