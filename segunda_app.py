import streamlit as st

def main():
    conversion_type = st.selectbox("Seleccione el tipo de conversión:", ["Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de Datos"])

    if conversion_type == "Temperatura":
        convert_temperature()
    elif conversion_type == "Longitud":
        convert_length()
    elif conversion_type == "Peso/Masa":
        convert_weight_mass()
    elif conversion_type == "Volumen":
        convert_volume()
    elif conversion_type == "Tiempo":
        convert_time()
    elif conversion_type == "Velocidad":
        convert_speed()
    elif conversion_type == "Área":
        convert_area()
    elif conversion_type == "Energía":
        convert_energy()
    elif conversion_type == "Presión":
        convert_pressure()
    elif conversion_type == "Tamaño de Datos":
        convert_data_size()

def convert_temperature():
    st.header("Conversión de Temperatura")
    temperature_options = [
        "Celsius a Fahrenheit", "Fahrenheit a Celsius",
        "Celsius a Kelvin", "Kelvin a Celsius"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", temperature_options)

    if selected_option == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingrese la temperatura en Celsius:", value=0.0)
        fahrenheit = (celsius * 9/5) + 32
        st.write(f"{celsius:.2f} °C equivale a {fahrenheit:.2f} °F")

    elif selected_option == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingrese la temperatura en Fahrenheit:", value=0.0)
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit:.2f} °F equivale a {celsius:.2f} °C")

    elif selected_option == "Celsius a Kelvin":
        celsius = st.number_input("Ingrese la temperatura en Celsius:", value=0.0)
        kelvin = celsius + 273.15
        st.write(f"{celsius:.2f} °C equivale a {kelvin:.2f} K")

    elif selected_option == "Kelvin a Celsius":
        kelvin = st.number_input("Ingrese la temperatura en Kelvin:", value=0.0)
        celsius = kelvin - 273.15
        st.write(f"{kelvin:.2f} K equivale a {celsius:.2f} °C")

# Implementa la función convert_length()
def convert_length():
    st.header("Conversión de Longitud")
    length_options = [
        "Pies a Metros", "Metros a Pies",
        "Pulgadas a Centímetros", "Centímetros a Pulgadas"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", length_options)

    if selected_option == "Pies a Metros":
        pies = st.number_input("Ingrese la longitud en pies:", value=0.0)
        metros = pies * 0.3048
        st.write(f"{pies:.2f} pies equivale a {metros:.2f} metros")

    elif selected_option == "Metros a Pies":
        metros = st.number_input("Ingrese la longitud en metros:", value=0.0)
        pies = metros / 0.3048
        st.write(f"{metros:.2f} metros equivale a {pies:.2f} pies")

    elif selected_option == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingrese la longitud en pulgadas:", value=0.0)
        centimetros = pulgadas * 2.54
        st.write(f"{pulgadas:.2f} pulgadas equivale a {centimetros:.2f} centímetros")

    elif selected_option == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingrese la longitud en centímetros:", value=0.0)
        pulgadas = centimetros / 2.54
        st.write(f"{centimetros:.2f} centímetros equivale a {pulgadas:.2f} pulgadas")

def convert_weight_mass():
    st.header("Conversión de Peso/Masa")
    weight_mass_options = [
        "Libras a Kilogramos", "Kilogramos a Libras",
        "Onzas a Gramos", "Gramos a Onzas"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", weight_mass_options)

    if selected_option == "Libras a Kilogramos":
        libras = st.number_input("Ingrese el peso en libras:", value=0.0)
        kilogramos = libras * 0.453592
        st.write(f"{libras:.2f} libras equivale a {kilogramos:.2f} kilogramos")

    elif selected_option == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingrese el peso en kilogramos:", value=0.0)
        libras = kilogramos / 0.453592
        st.write(f"{kilogramos:.2f} kilogramos equivale a {libras:.2f} libras")

    elif selected_option == "Onzas a Gramos":
        onzas = st.number_input("Ingrese el peso en onzas:", value=0.0)
        gramos = onzas * 28.3495
        st.write(f"{onzas:.2f} onzas equivale a {gramos:.2f} gramos")

    elif selected_option == "Gramos a Onzas":
        gramos = st.number_input("Ingrese el peso en gramos:", value=0.0)
        onzas = gramos / 28.3495
        st.write(f"{gramos:.2f} gramos equivale a {onzas:.2f} onzas")

def convert_volume():
    st.header("Conversión de Volumen")
    volume_options = [
        "Galones a Litros", "Litros a Galones",
        "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", volume_options)

    if selected_option == "Galones a Litros":
        galones = st.number_input("Ingrese el volumen en galones:", value=0.0)
        litros = galones * 3.78541
        st.write(f"{galones:.2f} galones equivale a {litros:.2f} litros")

    elif selected_option == "Litros a Galones":
        litros = st.number_input("Ingrese el volumen en litros:", value=0.0)
        galones = litros / 3.78541
        st.write(f"{litros:.2f} litros equivale a {galones:.2f} galones")

    elif selected_option == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingrese el volumen en pulgadas cúbicas:", value=0.0)
        cm_cubicos = pulgadas_cubicas * 16.3871
        st.write(f"{pulgadas_cubicas:.2f} pulgadas cúbicas equivale a {cm_cubicos:.2f} centímetros cúbicos")

    elif selected_option == "Centímetros cúbicos a Pulgadas cúbicas":
        cm_cubicos = st.number_input("Ingrese el volumen en centímetros cúbicos:", value=0.0)
        pulgadas_cubicas = cm_cubicos / 16.3871
        st.write(f"{cm_cubicos:.2f} centímetros cúbicos equivale a {pulgadas_cubicas:.2f} pulgadas cúbicas")

def convert_time():
    st.header("Conversión de Tiempo")
    time_options = [
        "Horas a Minutos", "Minutos a Segundos",
        "Días a Horas", "Semanas a Días"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", time_options)

    if selected_option == "Horas a Minutos":
        horas = st.number_input("Ingrese la cantidad de horas:", value=0.0)
        minutos = horas * 60
        st.write(f"{horas:.2f} horas equivale a {minutos:.2f} minutos")

    elif selected_option == "Minutos a Segundos":
        minutos = st.number_input("Ingrese la cantidad de minutos:", value=0.0)
        segundos = minutos * 60
        st.write(f"{minutos:.2f} minutos equivale a {segundos:.2f} segundos")

    elif selected_option == "Días a Horas":
        dias = st.number_input("Ingrese la cantidad de días:", value=0.0)
        horas = dias * 24
        st.write(f"{dias:.2f} días equivale a {horas:.2f} horas")

    elif selected_option == "Semanas a Días":
        semanas = st.number_input("Ingrese la cantidad de semanas:", value=0.0)
        dias = semanas * 7
        st.write(f"{semanas:.2f} semanas equivale a {dias:.2f} días")

def convert_speed():
    st.header("Conversión de Velocidad")
    speed_options = [
        "Millas por Hora a Kilómetros por Hora", "Kilómetros por Hora a Metros por Segundo",
        "Nudos a Millas por Hora", "Metros por Segundo a Pies por Segundo"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", speed_options)

    if selected_option == "Millas por Hora a Kilómetros por Hora":
        mph = st.number_input("Ingrese la velocidad en millas por hora:", value=0.0)
        kph = mph * 1.60934
        st.write(f"{mph:.2f} millas por hora equivale a {kph:.2f} kilómetros por hora")

    elif selected_option == "Kilómetros por Hora a Metros por Segundo":
        kph = st.number_input("Ingrese la velocidad en kilómetros por hora:", value=0.0)
        mps = kph * 0.277778
        st.write(f"{kph:.2f} kilómetros por hora equivale a {mps:.2f} metros por segundo")

    elif selected_option == "Nudos a Millas por Hora":
        nudos = st.number_input("Ingrese la velocidad en nudos:", value=0.0)
        mph = nudos * 1.15078
        st.write(f"{nudos:.2f} nudos equivale a {mph:.2f} millas por hora")

    elif selected_option == "Metros por Segundo a Pies por Segundo":
        mps = st.number_input("Ingrese la velocidad en metros por segundo:", value=0.0)
        fps = mps * 3.28084
        st.write(f"{mps:.2f} metros por segundo equivale a {fps:.2f} pies por segundo")

def convert_area():
    st.header("Conversión de Área")
    area_options = [
        "Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados",
        "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", area_options)

    if selected_option == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingrese el área en metros cuadrados:", value=0.0)
        pies_cuadrados = metros_cuadrados * 10.7639
        st.write(f"{metros_cuadrados:.2f} metros cuadrados equivale a {pies_cuadrados:.2f} pies cuadrados")

    elif selected_option == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingrese el área en pies cuadrados:", value=0.0)
        metros_cuadrados = pies_cuadrados / 10.7639
        st.write(f"{pies_cuadrados:.2f} pies cuadrados equivale a {metros_cuadrados:.2f} metros cuadrados")

    elif selected_option == "Kilómetros cuadrados a Millas cuadradas":
        km_cuadrados = st.number_input("Ingrese el área en kilómetros cuadrados:", value=0.0)
        millas_cuadradas = km_cuadrados * 0.386102
        st.write(f"{km_cuadrados:.2f} kilómetros cuadrados equivale a {millas_cuadradas:.2f} millas cuadradas")

    elif selected_option == "Millas cuadradas a Kilómetros cuadrados":
        millas_cuadradas = st.number_input("Ingrese el área en millas cuadradas:", value=0.0)
        km_cuadrados = millas_cuadradas / 0.386102
        st.write(f"{millas_cuadradas:.2f} millas cuadradas equivale a {km_cuadrados:.2f} kilómetros cuadrados")

def convert_energy():
    st.header("Conversión de Energía")
    energy_options = [
        "Julios a Calorías", "Calorías a Kilojulios",
        "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", energy_options)

    if selected_option == "Julios a Calorías":
        julios = st.number_input("Ingrese la energía en julios:", value=0.0)
        calorias = julios * 0.239006
        st.write(f"{julios:.2f} julios equivale a {calorias:.2f} calorías")

    elif selected_option == "Calorías a Kilojulios":
        calorias = st.number_input("Ingrese la energía en calorías:", value=0.0)
        kj = calorias * 0.0041868
        st.write(f"{calorias:.2f} calorías equivale a {kj:.4f} kilojulios")

    elif selected_option == "Kilovatios-hora a Megajulios":
        kw_hora = st.number_input("Ingrese la energía en kilovatios-hora:", value=0.0)
        mj = kw_hora * 3.6
        st.write(f"{kw_hora:.2f} kilovatios-hora equivale a {mj:.2f} megajulios")

    elif selected_option == "Megajulios a Kilovatios-hora":
        mj = st.number_input("Ingrese la energía en megajulios:", value=0.0)
        kw_hora = mj / 3.6
        st.write(f"{mj:.2f} megajulios equivale a {kw_hora:.2f} kilovatios-hora")

def convert_pressure():
    st.header("Conversión de Presión")
    pressure_options = [
        "Pascales a Atmósferas", "Atmósferas a Pascales",
        "Barras a Libras por Pulgada cuadrada", "Libras por Pulgada cuadrada a Barras"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", pressure_options)

    if selected_option == "Pascales a Atmósferas":
        pascales = st.number_input("Ingrese la presión en pascales:", value=0.0)
        atmosferas = pascales / 101325
        st.write(f"{pascales:.2f} pascales equivale a {atmosferas:.6f} atmósferas")

    elif selected_option == "Atmósferas a Pascales":
        atmosferas = st.number_input("Ingrese la presión en atmósferas:", value=0.0)
        pascales = atmosferas * 101325
        st.write(f"{atmosferas:.6f} atmósferas equivale a {pascales:.2f} pascales")

    elif selected_option == "Barras a Libras por Pulgada cuadrada":
        barras = st.number_input("Ingrese la presión en barras:", value=0.0)
        psi = barras * 14.5038
        st.write(f"{barras:.2f} barras equivale a {psi:.2f} libras por pulgada cuadrada")

    elif selected_option == "Libras por Pulgada cuadrada a Barras":
        psi = st.number_input("Ingrese la presión en libras por pulgada cuadrada:", value=0.0)
        barras = psi / 14.5038
        st.write(f"{psi:.2f} libras por pulgada cuadrada equivale a {barras:.2f} barras")

def convert_data_size():
    st.header("Conversión de Tamaño de Datos")
    data_size_options = [
        "Megabytes a Gigabytes", "Gigabytes a Terabytes",
        "Kilobytes a Megabytes", "Terabytes a Petabytes"
    ]
    selected_option = st.selectbox("Seleccione la conversión:", data_size_options)

    if selected_option == "Megabytes a Gigabytes":
        mb = st.number_input("Ingrese el tamaño en megabytes:", value=0.0)
        gb = mb / 1024
        st.write(f"{mb:.2f} megabytes equivale a {gb:.2f} gigabytes")

    elif selected_option == "Gigabytes a Terabytes":
        gb = st.number_input("Ingrese el tamaño en gigabytes:", value=0.0)
        tb = gb / 1024
        st.write(f"{gb:.2f} gigabytes equivale a {tb:.2f} terabytes")

    elif selected_option == "Kilobytes a Megabytes":
        kb = st.number_input("Ingrese el tamaño en kilobytes:", value=0.0)
        mb = kb / 1024
        st.write(f"{kb:.2f} kilobytes equivale a {mb:.2f} megabytes")

    elif selected_option == "Terabytes a Petabytes":
        tb = st.number_input("Ingrese el tamaño en terabytes:", value=0.0)
        pb = tb / 1024
        st.write(f"{tb:.2f} terabytes equivale a {pb:.2f} petabytes")

if __name__ == "__main__":
    st.title("Conversor de Unidades")
    st.write("Seleccione el tipo de conversión y complete las unidades para convertir.")
    main()
