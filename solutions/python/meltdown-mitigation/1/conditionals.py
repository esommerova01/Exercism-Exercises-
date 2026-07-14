"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    """Check reactor criticality."""
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500_000:
        return True
    else:
        return False
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zones."""
    generated_power = float(voltage) * float(current)
    efficiency = (generated_power/theoretical_max_power) * 100
    if efficiency >= 80: 
        return "green"
    elif efficiency >= 60: 
        return "orange"
    elif efficiency >= 30: 
        return "red"
    else: 
        return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    criticality = temperature * neutrons_produced_per_second
    if criticality < (0.9 * threshold): 
        return 'LOW'
    elif criticality < (1.1 * threshold): 
        return "NORMAL"
    else: 
        return "DANGER"