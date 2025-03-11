from s3_index.index import IndexManager


#######################################################
def setup_module():
	print("setup")


#######################################################
def teardown_module():
	print("teardown")


#######################################################
#######################################################
# @pytest.mark.skip(reason="requires prod credentials")
def test_build_merkle_tree():
	"""
	The goal of this test is to create a merkle tree of a s3 directory.
	It will iterate over each object, record the keys, the checksum, & the
	size and organize the information into a networkx graph
	"""
	input_bucket_name = "noaa-wcsd-pds"

	index_manager = IndexManager(input_bucket_name)

	foo = index_manager.build_merkle_tree()

	assert len(foo) > 0

def test_get_total_size():
	### files from here: https://docs.google.com/spreadsheets/d/1_mpVNaZI9hD3kG0P4cZIkG-TI6bCh9FTORPy3KfPq-o/edit?gid=0#gid=0
	prefixes = [
		f"data/raw/Henry_B._Bigelow/HB2405/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2404/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2403/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2402/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2401/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2305/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2304/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2303/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2302/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2301/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2206/EK60/",
		f"data/raw/Pisces/PC2205/EK80/",
		f"data/raw/Henry_B._Bigelow/HB2205/EK60/",
		f"data/raw/Henry_B._Bigelow/HB2204/EK60/",
		f"data/raw/Henry_B._Bigelow/HB2203/EK60/",
		f"data/raw/Henry_B._Bigelow/HB2202/EK60/",
		f"data/raw/Henry_B._Bigelow/HB2103/EK60/",
		f"data/raw/Henry_B._Bigelow/HB2102/EK60/",
		f"data/raw/Pisces/PC2104/EK60/",
		f"data/raw/Henry_B._Bigelow/HB2101/EK60/",
		f"data/raw/Henry_B._Bigelow/HB2001/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1906/EK60/",
		f"data/raw/Gordon_Gunter/GU1905/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1904/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1907/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1903/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1902/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1901/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1806/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1805/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1803/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1802/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1801/EK60/",
		f"data/raw/Pisces/PC1706/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1702/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1701/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1604/EK60/",
		f"data/raw/Pisces/PC1609/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1603/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1601/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1507/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1506/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1503/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1502/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1501/EK60/",
		f"data/raw/Pisces/PC1405/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1405/EK60/",
		f"data/raw/Pisces/PC1404/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1403/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1402/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1401/EK60/",
		f"data/raw/Gordon_Gunter/GU1402L1/EK60/", # L1 and L2
		f"data/raw/Gordon_Gunter/GU1402L2/EK60/",
		f"data/raw/Gordon_Gunter/GU1305/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1304/EK60/",
		f"data/raw/Okeanos_Explorer/EX1305/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1303/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1301/EK60/",
		f"data/raw/Pisces/PC1301/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1206/EK60/",
		f"data/raw/Pisces/PC1206/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1201/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1105/EK60/",
		f"data/raw/Delaware_Ii/DE1108/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1103/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1102/EK60/",
		f"data/raw/Delaware_Ii/DE1010/EK60/",
		f"data/raw/Henry_B._Bigelow/HB1006/EK60/",
		# f"data/raw/Delaware_Ii/DE0107/EK60/", # EK500 not EK60?
		f"data/raw/Delaware_Ii/DE0107/EK500/",
		f"data/raw/Henry_B._Bigelow/HB1002/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0905/EK60/",
		f"data/raw/Delaware_Ii/DE0910/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0904/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0903/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0902/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0901/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0807/EK60/",
		f"data/raw/Albatross_Iv/AL0803/EK60/",
		#f"data/raw/Delaware_Ii/DE0809/EK60/", # EK500 not EK60?
		f"data/raw/Delaware_Ii/DE0809/EK500/",
		f"data/raw/Henry_B._Bigelow/HB0806/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0805/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0803/EK60/",
		f"data/raw/Albatross_Iv/AL0801/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0802/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0711/EK60/",
		f"data/raw/Delaware_Ii/DE0710/EK500/",
		f"data/raw/Henry_B._Bigelow/HB0710/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0706/EK60/",
		f"data/raw/Henry_B._Bigelow/HB0707/EK60/",
		f"data/raw/Delaware_Ii/DE0615/EK500/",
		f"data/raw/Albatross_Iv/AL0509/EK60/",
		f"data/raw/Albatross_Iv/AL0508/EK60/",
		f"data/raw/Delaware_Ii/DE0512/EK500/",
		f"data/raw/Delaware_Ii/DE0505/EK500/",
		f"data/raw/Albatross_Iv/AL0504/EK60/",
		f"data/raw/Albatross_Iv/AL0502/EK60/",
		f"data/raw/Albatross_Iv/AL0409/EK60/",
		f"data/raw/Delaware_Ii/DE0413/EK500/",
		f"data/raw/Delaware_Ii/DE0410/EK500/",
		f"data/raw/Delaware_Ii/DE0408/EK500/",
		f"data/raw/Albatross_Iv/AL0404/EK60/",
		f"data/raw/Albatross_Iv/AL0403/EK60/",
		f"data/raw/Albatross_Iv/AL0401/EK60/",
		f"data/raw/Albatross_Iv/AL0305/EK60/",
		# f"data/raw/Albatross_Iv/AL0308/EK60/", # isn't found in noaa-wcsd-pds
		f"data/raw/Albatross_Iv/AL0304/EK60/",
		f"data/raw/Delaware_Ii/DE0306/EK500/",
		f"data/raw/Delaware_Ii/DE0303/EK500/",
		f"data/raw/Delaware_Ii/DE0302/EK500/",
		f"data/raw/Delaware_Ii/DE0301/EK500/",
		f"data/raw/Albatross_Iv/AL0210/EK500/",
		f"data/raw/Delaware_Ii/DE0208/EK500/",
		f"data/raw/Delaware_Ii/DE0206/EK500/",
		f"data/raw/Albatross_Iv/AL0207/EK500/",
		f"data/raw/Albatross_Iv/AL0204/EK500/",
		f"data/raw/Delaware_Ii/DE0201/EK500/",
		f"data/raw/Albatross_Iv/AL0203/EK500/",
		f"data/raw/Albatross_Iv/AL0110/EK500/",
		f"data/raw/Delaware_Ii/DE0109/EK500/",
		f"data/raw/Delaware_Ii/DE0108/EK500/",
		f"data/raw/Albatross_Iv/AL0105/EK500/",
		f"data/raw/Albatross_Iv/AL0104/EK500/",
		f"data/raw/Albatross_Iv/AL0103/EK500/",
		f"data/raw/Albatross_Iv/AL0102/EK500/",
		f"data/raw/Delaware_Ii/DE0101/EK500/",
		f"data/raw/Albatross_Iv/AL0007/EK500/",
		f"data/raw/Albatross_Iv/AL0006/EK500/",
		f"data/raw/Delaware_Ii/DE0008/EK500/",
		f"data/raw/Delaware_Ii/DE0007/EK500/",
		f"data/raw/Delaware_Ii/DE0005/EK500/",
		f"data/raw/Albatross_Iv/AL0002/EK500/",
		f"data/raw/Albatross_Iv/AL0001/EK500/",
		f"data/raw/Delaware_Ii/DE0002/EK500/",
		f"data/raw/Albatross_Iv/AL9911/EK500/",
		f"data/raw/Delaware_Ii/DE9909/EK500/",
		f"data/raw/Delaware_Ii/DE9908/EK500/",
		f"data/raw/Delaware_Ii/DE9906/EK500/",
		f"data/raw/Albatross_Iv/AL9903/EK500/",
		f"data/raw/Delaware_Ii/DE9903/EK500/",
		f"data/raw/Albatross_Iv/AL9902/EK500/",
		f"data/raw/Albatross_Iv/AL9811/EK500/",
		f"data/raw/Delaware_Ii/DE9810/EK500/",
		f"data/raw/Delaware_Ii/DE9809/EK500/",
		f"data/raw/Albatross_Iv/AL9804/EK500/"
	]
	# prefixes = [
	# 	f"data/raw/Henry_B._Bigelow/HB1906/EK60/",
	# ]
	index_manager = IndexManager("noaa-wcsd-pds")
	index_manager.get_total_size(prefixes=prefixes)
	# assert len(foo) > 0

def test_get_total_size_henry_bigelow():
	# files from here: https://docs.google.com/spreadsheets/d/1_mpVNaZI9hD3kG0P4cZIkG-TI6bCh9FTORPy3KfPq-o/edit?gid=0#gid=0
	prefixes = [
		f"data/raw/Henry_B._Bigelow/"
	]
	index_manager = IndexManager("noaa-wcsd-pds")
	index_manager.get_total_size(prefixes=prefixes)

def test_index_s3_bucket():
	index_manager = IndexManager("noaa-wcsd-pds")
	index_manager.index_s3_bucket()


#######################################################
'''    
HB2405	EK80	Bigelow
HB2404	EK80	Bigelow
HB2403	EK80	Bigelow
HB2402	EK80	Bigelow
HB2401	EK80	Bigelow
HB2305	EK80	Bigelow
HB2304	EK80	Bigelow
HB2303	EK80	Bigelow
HB2302	EK80	Bigelow
HB2301	EK80	Bigelow
HB2206	EK60	Bigelow
PC2205	EK80	Pisces
HB2205	EK60	Bigelow
HB2204	EK60	Bigelow
HB2203	EK60	Bigelow
HB2202	EK60	Bigelow
HB2103	EK60	Bigelow
HB2102	EK60	Bigelow
PC2104	EK60	Pisces
HB2101	EK60	Bigelow
HB2001	EK60	Bigelow
HB1906	EK60	Bigelow
GU1905	EK60	Gunter
HB1904	EK60	Bigelow
HB1907	EK60	Bigelow
HB1903	EK60	Bigelow
HB1902	EK60	Bigelow
HB1901	EK60	Bigelow
HB1806	EK60	Bigelow
HB1805	EK60	Bigelow
HB1803	EK60	Bigelow
HB1802	EK60	Bigelow
HB1801	EK60	Bigelow
PC1706	EK60	Pisces
HB1702	EK60	Bigelow
HB1701	EK60	Bigelow
HB1604	EK60	Bigelow
PC1609	EK60	Pisces
HB1603	EK60	Bigelow
HB1601	EK60	Bigelow
HB1507	EK60	Bigelow
HB1506	EK60	Bigelow
HB1503	EK60	Bigelow
HB1502	EK60	Bigelow
HB1501	EK60	Bigelow
PC1405	EK60	Pisces
HB1405	EK60	Bigelow
PC1404	EK60	Pisces
HB1403	EK60	Bigelow
HB1402	EK60	Bigelow
HB1401	EK60	Bigelow
GU1402	EK60	Gunter
GU1305	EK60	Gunter
HB1304	EK60	Bigelow
EX1305	EK60	Okeanos
HB1303	EK60	Bigelow
HB1301	EK60	Bigelow
PC1301	EK60	Pisces
HB1206	EK60	Bigelow
PC1206	EK60	Pisces
HB1201	EK60	Bigelow
HB1105	EK60	Bigelow
DE1108	EK60	Delaware
HB1103	EK60	Bigelow
HB1102	EK60	Bigelow
DE1010	EK60	Delaware
HB1006	EK60	Bigelow
DE0107	EK60	Delaware
HB1002	EK60	Bigelow
HB0905	EK60	Bigelow
DE0910	EK60	Delaware
HB0904	EK60	Bigelow
HB0903	EK60	Bigelow
HB0902	EK60	Bigelow
HB0901	EK60	Bigelow
HB0807	EK60	Bigelow
AL0803	EK60	Albatross
DE0809	EK60	Delaware
HB0806	EK60	Bigelow
HB0805	EK60	Bigelow
HB0803	EK60	Bigelow
AL0801	EK60	Albatross
HB0802	EK60	Bigelow
HB0711	EK60	Bigelow
DE0710	EK500	Delaware
HB0710	EK60	Bigelow
HB0706	EK60	Bigelow
HB0707	EK60	Bigelow
DE0615	EK500	Delaware
AL0509	EK60	Albatross
AL0508	EK60	Albatross
DE0512	EK500	Delaware
DE0505	EK500	Delaware
AL0504	EK60	Albatross
AL0502	EK60	Albatross
AL0409	EK60	Albatross
DE0413	EK500	Delaware
DE0410	EK500	Delaware
DE0408	EK500	Delaware
AL0404	EK60	Albatross
AL0403	EK60	Albatross
AL0401	EK60	Albatross
AL0305	EK60	Albatross
AL0308	EK60	Albatross
AL0304	EK60	Albatross
DE0306	EK500	Delaware
DE0303	EK500	Delaware
DE0302	EK500	Delaware
DE0301	EK500	Delaware
AL0210	EK500	Albatross
DE0208	EK500	Delaware
DE0206	EK500	Delaware
AL0207	EK500	Albatross
AL0204	EK500	Albatross
DE0201	EK500	Delaware
AL0203	EK500	Albatross
AL0110	EK500	Albatross
DE0109	EK500	Delaware
DE0108	EK500	Delaware
AL0105	EK500	Albatross
AL0104	EK500	Albatross
AL0103	EK500	Albatross
AL0102	EK500	Albatross
DE0101	EK500	Delaware
AL0007	EK500	Albatross
AL0006	EK500	Albatross
DE0008	EK500	Delaware
DE0007	EK500	Delaware
DE0005	EK500	Delaware
AL0002	EK500	Albatross
AL0001	EK500	Albatross
DE0002	EK500	Delaware
AL9911	EK500	Albatross
DE9909	EK500	Delaware
DE9908	EK500	Delaware
DE9906	EK500	Delaware
AL9903	EK500	Albatross
DE9903	EK500	Delaware
AL9902	EK500	Albatross
AL9811	EK500	Albatross
DE9810	EK500	Delaware
DE9809	EK500	Delaware
AL9804	EK500	Albatross 
    '''
#######################################################
