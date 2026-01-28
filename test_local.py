from etl.extract import extract_excel
from etl.transform import (
    apply_quality_rules,
    calculate_metrics,
    segment_customers,
    generate_summaries
)


df = extract_excel("data/input/crm_interactions.xlsx")
print("RAW:")
print(df)

df = apply_quality_rules(df)
print("\nAFTER QUALITY:")
print(df)

metrics = calculate_metrics(df)
print("\nMETRICS:")
print(metrics)

metrics = segment_customers(metrics)
metrics = generate_summaries(metrics)

print("\nFINAL:")
print(metrics)
