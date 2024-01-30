# My Car
car_model = "Chevrolet Cruze"
year = 2014
engine_size = 1.4
car_size = (4514, "x", 1797, "x", 1477)
corrent_speed = [80,81,82]
factory_colors = {"black", "Gray", "Green"}
drivers_list = {"name" : "Samvel Manvelyan" , "age" : 35 , "license type" : "b , c" }
sunroof = False

# My Car converting  to int
car_model = "Chevrolet Cruze" # not Convertible to int
year = 2014
engine_size = int(1.4)
car_size = (4514, 1797, 1477) #  int() argument must be a string, a bytes-like object or a real number, not 'tuple'
corrent_speed = [80,81,82] # int() argument must be a string, a bytes-like object or a real number, not 'list'
factory_colors = {"black", "Gray", "Green"} # int() argument must be a string, a bytes-like object or a real number, not 'set'
drivers_list = {"name" : "Samvel Manvelyan" , "age" : 35 , "license type" : "b , c" } # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
sunroof = False

# My Car converting to String
car_model = "Chevrolet Cruze"
year = str(2014)
engine_size = str(1.4)
car_size =str((4514, "x", 1797, "x", 1477))
corrent_speed = str([80,81,82])
factory_colors = str({"black", "Gray", "Green"})
drivers_list = str({"name" : "Samvel Manvelyan" , "age" : 35 , "license type" : "b , c" })
sunroof = False

# My Car to float
car_model = "Chevrolet Cruze" # could not convert string to float: 'Chevrolet Cruze'
year = float(2014)
engine_size = 1.4
car_size = (4514, "x", 1797, "x", 1477) # float() argument must be a string or a real number, not 'tuple'
corrent_speed = [80,81,82] #float() argument must be a string or a real number, not 'list'
factory_colors = {"black", "Gray", "Green"} # float() argument must be a string or a real number, not 'set'
drivers_list = {"name" : "Samvel Manvelyan" , "age" : 35 , "license type" : "b , c" }  # float() argument must be a string or a real number, not 'dict'
sunroof = False