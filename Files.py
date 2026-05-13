import csv
from Multilist import LinkedList
from country import Country
from departament import Departament
from city import City


class Files():
    def read_file(self, path):

        multilista = LinkedList()
        colombia = Country("CO", "Colombia")
        multilista.append(colombia)

        departamentos = {}

        with open(path, encoding="utf-8-sig") as file:
            
            reader = csv.DictReader(file)

            for row in reader:
                dept_code = row["cod_depto"]
                dept_name = row["departamento"]

                city_code = row["cod_mpio"]
                city_name = row["municipio"]

                lat = row["lat"]
                lon = row["lon"]
                
                if dept_code not in departamentos:
                    department = Departament(dept_code, dept_name)

                    multilista.add_child(
                        colombia,
                        department                                                      
                    )

                    departamentos[dept_code] = department

                    city = City(
                        city_code,
                        city_name,
                        lat,
                        lon
                    )

                    multilista.add_child(
                        departamentos[dept_code],
                        city
                    )
            return multilista
    def get_markers(self, multilist):
        markers = []

        current_country = multilist.head

        while current_country:
            if current_country.sub_list:
                current_department = current_country.sub_list.head

                while current_department:
                    if current_department.sub_list:
                        current_city = current_department.sub_list.head

                        while current_city:
                            markers.append({
                                "lat": current_city.lat,
                                "lon": current_city.lon,
                                "popup": f"""
                                <b>{current_city.name}</b><br>
                                Departamento:
                                {current_department.name}
                                """
                                })   

                            current_city = current_city.next

                    current_department = current_department.next

            current_country = current_country.next

        return markers