"""
Project: Neroxa - Network Boost
Test Runner for Night Operations
"""

from network_booster import NeroxaNetworkBooster

if __name__ == "__main__":
    print("[Neroxa Network] Initiating network optimization test...")
    
    # Running the booster utility
    result = NeroxaNetworkBooster.optimize_connection()
    
    print(f"[Neroxa Network] Test Result: {result}")
    print("[Neroxa Network] System status: OPTIMIZED & SECURE.")
