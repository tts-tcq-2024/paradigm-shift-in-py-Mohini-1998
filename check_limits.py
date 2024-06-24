
def battery_is_ok(temperature, soc, charge_rate):
  if temperature in not(range(0,46)) :
    print('Temperature is out of range!')
    return False
  elif soc in not(range(20,81)) :
    print('State of Charge is out of range!')
    return False
  elif charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False

  return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
