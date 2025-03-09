import asyncio
from weather import get_alerts, get_forecast

async def main():
    # Test get_alerts
    print("Testing get_alerts for California...")
    alerts = await get_alerts("CA")
    print("\nALERTS RESULT:")
    print(alerts)
    
    # Test get_forecast for San Francisco
    print("\nTesting get_forecast for San Francisco...")
    forecast = await get_forecast(37.7749, -122.4194)
    print("\nFORECAST RESULT:")
    print(forecast)

if __name__ == "__main__":
    asyncio.run(main())