import aspose.pycore as aspycore
from aspose.imaging import Metered


# ExStart:MeteredLicensing
# Create an instance of Imaging Metered class
metered = Metered()
# Access the set_metered_key property and pass public and private keys as parameters
metered.set_metered_key("*****", "*****")
# Get metered data amount before calling API
amount_before = Metered.get_consumption_quantity()
# Display information
print("Amount Consumed Before:", amount_before)

# Do something

# Get metered data amount After calling API
amount_after = Metered.get_consumption_quantity()
# Display information
print("Amount Consumed After:", amount_after)
