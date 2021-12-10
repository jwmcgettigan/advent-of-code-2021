def get_mock_diagnostic_report():
  with open('mock_input.txt') as file:
    return file.read().splitlines()

def get_diagnostic_report():
  with open('input.txt') as file:
    return file.read().splitlines()

# part 1

def get_all_bits(diagnostic_report):
  all_bits = []
  for i in range(len(diagnostic_report[0])):
    all_bits.append(list(map(int, [x[i] for x in diagnostic_report])))
  return all_bits

def get_most_common_bit(bits):
  return int(bits.count(1) > bits.count(0))

def get_power_consumption():
  most_common_bits = ""
  least_common_bits = ""

  for bits in get_all_bits(get_diagnostic_report()):
    most_common_bit = get_most_common_bit(bits)
    most_common_bits += str(most_common_bit)
    least_common_bits += str(int(not bool(most_common_bit)))

  gamma_rate = int(most_common_bits, 2)
  epsilon_rate = int(least_common_bits, 2)
  return gamma_rate * epsilon_rate

#print(get_power_consumption())

# part 2

def get_bit_commonality(bits):
  ones, zeros = bits.count(1), bits.count(0)
  most_common, least_common = int(ones >= zeros), int(ones < zeros)
  #print(f'ones: {ones}, zeros: {zeros}, most: {most_common}, least: {least_common}')
  return (most_common, least_common)

def process_oxygen_generator_report(i, report):
  bit_list = []
  for bits in report:
    bit_list.append(int(bits[i]))
  (most_common, least_common) = get_bit_commonality(bit_list)
  return [bits for bits in report if int(bits[i]) == most_common]

def process_co2_scrubber_report(i, report):
  bit_list = []
  for bits in report:
    bit_list.append(int(bits[i]))
  (most_common, least_common) = get_bit_commonality(bit_list)
  return [bits for bits in report if int(bits[i]) == least_common]

def get_life_support_rating(report):
  oxygen_generator_report = report.copy()
  co2_scrubber_report = report.copy()
  
  for i in range(len(report[0])):
    if(len(oxygen_generator_report) > 1):
      oxygen_generator_report = process_oxygen_generator_report(i, oxygen_generator_report)

    if(len(co2_scrubber_report) > 1):
      co2_scrubber_report = process_co2_scrubber_report(i, co2_scrubber_report)

  oxygen_generator_rating = int(oxygen_generator_report[0], 2)
  co2_scrubber_rating = int(co2_scrubber_report[0], 2)

  return oxygen_generator_rating * co2_scrubber_rating

print(get_life_support_rating(get_diagnostic_report()))