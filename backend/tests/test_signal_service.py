from app.services.signal_service import SignalService

service = SignalService()

report = service.generate_signal()

print("=" * 60)
print("FOREXMIND AI SIGNAL SERVICE")
print("=" * 60)

for key, value in report.items():
    print(f"{key}: {value}")