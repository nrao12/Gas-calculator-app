
import streamlit as st

def invasive_ventilator_calculator():
    st.subheader("Invasive Ventilator Gas Consumption Calculator")

    ventilator_type = st.selectbox("Ventilator Type", ["Servo-U", "Drager VN500", "Other"])
    mode = st.selectbox("Mode", ["VC", "PC", "SIMV", "Other"])
    weight = st.number_input("Patient Weight (kg)", min_value=0.0, step=0.1)
    tidal_volume = st.number_input("Tidal Volume (ml/kg)", min_value=0.0, step=0.1)
    rate = st.number_input("Ventilation Rate (breaths/min)", min_value=0.0, step=1.0)
    fio2 = st.slider("Oxygen % (FiO2)", min_value=21, max_value=100, value=40)

    st.markdown("### Calculated Gas Consumption")

    if weight > 0 and tidal_volume > 0 and rate > 0:
        minute_volume = (weight * tidal_volume / 1000) * rate  # in L/min
        oxygen_flow = minute_volume * (fio2 / 100)
        air_flow = minute_volume * (1 - fio2 / 100)

        st.write(f"Minute Volume: {minute_volume:.2f} L/min")
        st.write(f"Oxygen Flow: {oxygen_flow:.2f} L/min")
        st.write(f"Air Flow: {air_flow:.2f} L/min")
    else:
        st.info("Please enter valid values for weight, tidal volume, and rate.")

def high_flow_calculator():
    st.subheader("High Flow CPAP Gas Consumption Calculator")

    fio2 = st.slider("Oxygen % (FiO2)", min_value=21, max_value=100, value=40)
    journey_time = st.number_input("Journey Time (mins)", min_value=1, step=1, value=60)
    set_flow = st.number_input("Set Flow (L/min)", min_value=0.1, step=0.1, value=8.0)

    if 21 <= fio2 <= 100 and set_flow > 0:
        # FiO2 formula based on air-oxygen blending
        o2_ratio = (fio2 - 21) / (100 - 21)  # Blending ratio
        o2_flow = set_flow * o2_ratio
        air_flow = set_flow - o2_flow

        total_o2 = o2_flow * journey_time
        total_air = air_flow * journey_time

        st.markdown("### Calculated Flow Rates")
        st.write(f"O2 Flow: {o2_flow:.2f} L/min")
        st.write(f"Air Flow: {air_flow:.2f} L/min")
        st.markdown("### Total Gas Required for Journey")
        st.write(f"Total O2 Required: {total_o2:.2f} Litres")
        st.write(f"Total Air Required: {total_air:.2f} Litres")
    else:
        st.info("Please enter valid values for FiO2 and Set Flow.")

def main():
    st.title("Advanced Gas Consumption Calculator")

    tab1, tab2 = st.tabs(["Invasive Ventilator", "High Flow CPAP"])

    with tab1:
        invasive_ventilator_calculator()
    with tab2:
        high_flow_calculator()

if __name__ == "__main__":
    main()
