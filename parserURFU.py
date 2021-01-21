from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

ID_MT = '108654047'
SUPP_MT = 2
FILE_MT = 'MT.csv'

ID_KN = '404750216'
SUPP_KN = 11
FILE_KN = 'KN.csv'

ID_MMM = '409494257'
SUPP_MMM = 5

ID_PM = '368047210'
SUPP_PM = 8

ID_FIIT = '190174734'
SUPP_FIIT = 14

ID_MOAIS = '2104914128'
SUPP_MOAIS = 17

ID_FIZ = '331019439'
SUPP_FIZ = 59

ID_AST = '381568187'
SUPP_AST = 65

ID_KB = '523505269'
SUPP_KB = 128

ID_GEO = '614621391'
SUPP_GEO = 137

ID_MET = '1655874659'
SUPP_MET = 146

ID_INN = '974856908'
SUPP_INN = 155

ID_NANO = '1839949664'
SUPP_NANO = 164

ID_KIB = '1697608895'
SUPP_KIB = 191

#ирит-ртф

ID_IVT = '1643199238'
SUPP_IVT = 5

ID_PI = '718248420'
SUPP_PI = 17

ID_PRI = '973665143'
SUPP_PRI = 26

ID_BKS = '2085945490'
SUPP_BKS = 35

ID_IBS = '1394939152'
SUPP_IBT = 44

ID_IASB = '592540034'
SUPP_IASB = 53

ID_R = '1357573466'
SUPP_R = 62

ID_ITIS = '720421465'
SUPP_ITIS = 71

ID_KIT = '1592439947'
SUPP_KIT = 80




class urfuParser(object):
	def __init__(self, driver):
		self.driver = driver

	def parse(self):
		self.open_ajax()
		

		mt, total_area_mt_sub = self.parseIenim(ID_MT, SUPP_MT)
		kn, total_area_kn_sub = self.parseIenim(ID_KN, SUPP_KN)
		pm, total_area_pm_sub = self.parseIenim(ID_PM, SUPP_PM)
		ft, total_area_ft_sub = self.parseIenim(ID_FIIT, SUPP_FIIT)
		mo, total_area_mo_sub = self.parseIenim(ID_MOAIS, SUPP_MOAIS)
		mm, total_area_mm_sub = self.parseIenim(ID_MMM, SUPP_MMM)
		
		total_area_mt = 40
		total_area_kn = 60
		total_area_ft = 62
		total_area_pm = 12
		total_area_mo = 24
		total_area_mm = 20

		my_name = 'Султанов Артём Евгеньевич'
		rivals = {}

		kn_copy = kn.copy()
		for name_kn, total_kn in kn.items():
			if total_area_kn == 0:
				break
			if (name_kn in ft) and total_area_ft > 0:
				ft_keys = ft.keys()
				for name_ft in list(ft_keys):
					if name_ft == name_kn:
						total_area_ft -= 1
						del ft[name_ft]
						del kn_copy[name_kn]
						break
					del ft[name_ft]
					total_area_ft -= 1
			elif total_area_kn > 0:
				total_area_kn -= 1

		mt_copy = mt.copy()
		total_area_kn = 60
		for name_mt, total_mt in mt.items():
			if name_mt == my_name:
				rivals.update({
					name_mt: total_mt 
					})
				break

			if (name_mt in kn_copy) and total_area_kn > 0:
				kn_keys = kn_copy.keys()
				for name_kn in list(kn_keys):
					if name_kn == name_mt:
						total_area_kn -= 1
						del kn_copy[name_kn]
						# del mt_copy[name_mt]
						break
					del kn_copy[name_kn]
					total_area_kn -= 1
			else:
				rivals.update({
					name_mt: total_mt 
					})

		# iter_rival = 1
		# for name_rival, total_rival in rivals.items():
		# 	print(f'{iter_rival}. {name_rival} {total_rival}')
		# 	iter_rival += 1
		dict_rivals = rivals
		total_area_mt = 40
		total_area_kn = 60
		total_area_ft = 62

		for name_rival in rivals:
			for name_anon in kn:
				kn_list = list(kn.keys())
				pos = 0
				if name_rival == name_anon:
					for i in range(len(kn_list)):
						if name_rival == kn_list[i]:
							pos = i+1
					dict_rivals.update({
						name_rival: str(rivals[name_rival]) + f' КН({pos}/{total_area_kn})' 
					})
			for name_anon in ft:
				ft_list = list(ft.keys())
				pos = 0
				if name_rival == name_anon:
					for i in range(len(ft_list)):
						if name_rival == ft_list[i]:
							pos = i+1
					dict_rivals.update({
						name_rival: str(rivals[name_rival]) + f' ФИИТ({pos}/{total_area_ft})' 
					})
			for name_anon in mo:
				mo_list = list(mo.keys())
				pos = 0
				if name_rival == name_anon:
					for i in range(len(mo_list)):
						if name_rival == mo_list[i]:
							pos = i+1
					dict_rivals.update({
						name_rival: str(rivals[name_rival]) + f' МОАИС({pos}/{total_area_mo})' 
					})
			for name_anon in pm:
				pm_list = list(pm.keys())
				pos = 0
				if name_rival == name_anon:
					for i in range(len(pm_list)):
						if name_rival == pm_list[i]:
							pos = i+1
					dict_rivals.update({
						name_rival: str(rivals[name_rival]) + f' ПМ({pos}/{total_area_pm})' 
					})
			for name_anon in mm:
				mm_list = list(mm.keys())
				pos = 0
				if name_rival == name_anon:
					for i in range(len(mm_list)):
						if name_rival == mm_list[i]:
							pos = i+1
					dict_rivals.update({
						name_rival: str(rivals[name_rival]) + f' МХ({pos}/{total_area_mm})' 
					})

		iter_rival = 1
		for name_rival, value_rival in dict_rivals.items():
			print(f'{iter_rival}. {name_rival} - {value_rival}')
			iter_rival += 1

		with open('list.txt', 'w') as f:
			iter_rival = 1
			for name_rival, value_rival in dict_rivals.items():
				f.write(f'{iter_rival}. {name_rival} - {value_rival}\n')
				iter_rival += 1




		# print(f'MT KN: {len(list(set(mt) & set(kn)))}')
		# print(f'MT FIIT: {len(list(set(mt) & set(ft)))}')
		# print(f'KN FIIT: {len(list(set(kn) & set(ft)))}')
		# print(f'MT KN FIIT: {len(list(set(mt) & set(kn) & set(ft)))}')
		# print(f'MT KN PM: {len(list(set(mt) & set(kn) & set(pm)))}')
		# print(f'MT KN MOAIS: {len(list(set(mt) & set(kn) & set(pm)))}')


		# self.save_data(self.parseIenim(ID_MT, SUPP_MT), FILE_MT)
		# print('MT saved')

		# self.save_data(self.parseIenim(ID_KN, SUPP_KN), FILE_KN)
		# print('KN saved')

	# def parseKn(self):
	# 	#kn = self.driver.find_element_by_id(ID_KN)
	# 	#kn_count = kn.find_elements_by_tag_name('b')[1].text.split('заявлений - ')[1].replace(')', '')
	# 	kn = self.driver.find_elements_by_class_name('supp')[SUPP_KN]
	# 	kn = kn.find_elements_by_tag_name('tr')[2:]

	# 	dict_kn = []

	# 	for elem in kn:
	# 		name = elem.find_elements_by_tag_name('td')[0].text
	# 		total = elem.find_elements_by_tag_name('td')[-1].text

	# 		if '(' in name:
	# 			cons = 'Да'
	# 		else:
	# 			cons = ' '

	# 		dict_kn.append({
	# 			'name': name,
	# 			'consent': cons,
	# 			'total': total
	# 		})
	# 	return dict_kn


	def parseIenim(self, id_ienim, supp_ienim):
		wait = WebDriverWait(self.driver, 60)
		ienim = wait.until(EC.presence_of_element_located((By.ID, id_ienim)))
		total_area = int(ienim.find_elements_by_tag_name('b')[1].text.split('заявлений - ')[1].replace(')', ''))
		ienim = self.driver.find_elements_by_class_name('supp')[supp_ienim]
		ienim = ienim.find_elements_by_tag_name('tr')[2:]

		dict_ienim = {}

		for elem in ienim:
			name = str(elem.find_elements_by_tag_name('td')[0].text)
			#dict_ienim.append(name)
			total = elem.find_elements_by_tag_name('td')[-1].text
			dict_ienim.update({
				name: total
			})

			# if '(' in name:
			# 	cons = 'Да'
			# else:
			# 	cons = ' '

			# dict_ienim.append({
			# 	'name': name,
			# 	'consent': cons,
			# 	'total': total
			# })

		return dict_ienim, total_area

	def save_data(self, items, path):
		with open(path, 'w', newline='') as file:
			writer = csv.writer(file, delimiter=';')
			writer.writerow(['ФИО', 'СОГЛАСИЕ', 'БАЛЛЫ'])
			
			for item in items:
				writer.writerow([item['name'], item['consent'], item['total']])


	def open_ajax(self):
		self.driver.get('https://urfu.ru/ru/ratings/')

		wait = WebDriverWait(self.driver, 60)
		ienim_btn = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Очная")))
		ienim_btn.click()


def main():
	driver = webdriver.Chrome("/bin/chromedriver")

	parser = urfuParser(driver)
	parser.parse()

if __name__ == "__main__":
	main()