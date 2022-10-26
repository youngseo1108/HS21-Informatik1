def fine_calculator(area,speed):
	areas = ['urban', 'expressway', 'motorway']
	if type(area) != str:
		return 'Invalid Area Type'

	if area not in areas:
		return 'Invalid Area Value'

	if type(speed) == int or type(speed) == float:
		pass
	else:
		return 'Invalid Speed Type'

	if speed < 0:
		return 'Invalid Speed Value'
	
	if area == 'urban' and speed > 50:
		return round(1 * ((speed/50 - 1)*100)**2)
	
	if area == 'expressway' and speed > 100:
		return round(0.8 * ((speed/100 - 1)*100)**2)

	if area == 'motorway' and speed > 120:
		return round(0.5 * ((speed/120 - 1)*100)**2)
	return 0


print(fine_calculator(1,1)) # Invalid Area Type
print(fine_calculator('Zurich', 90)) # Invalid Area Value
print(fine_calculator('Urban', 8j)) # Invalid Speed Type
print(fine_calculator('urban', -10)) # Invalid Speed Value
print(fine_calculator('urban', 90))
print(fine_calculator('expressway', 120.0))
print(fine_calculator('motorway', 180))
print(fine_calculator('motorway', 120))