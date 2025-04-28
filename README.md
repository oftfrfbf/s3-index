# s3-index
iterates through and s3 bucket's objects and gets size and checksum information


# Installing Dependencies
```
uv pip install --upgrade pip
uv pip install -r pyproject.toml --extra dev
```

# SonarAI Object Backup
These are the paths in the s3://noaa-wcsd-pds bucket along with number of objects and the total size:
```commandline
WIP 20250312
data/raw/Henry_B._Bigelow/HB2405/EK80/
# aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB2405/EK80/ data/raw/Henry_B._Bigelow/HB2405/EK80/
Total objects: 176
Total size: 32.99 GB
data/raw/Henry_B._Bigelow/HB2404/EK80/
Total objects: 246
Total size: 48.02 GB
data/raw/Henry_B._Bigelow/HB2403/EK80/
Total objects: 372
Total size: 69.69 GB
data/raw/Henry_B._Bigelow/HB2402/EK80/
Total objects: 1648
Total size: 302.28 GB
data/raw/Henry_B._Bigelow/HB2401/EK80/
Total objects: 212
Total size: 41.23 GB
data/raw/Henry_B._Bigelow/HB2305/EK80/
Total objects: 11733
Total size: 1.35 TB
data/raw/Henry_B._Bigelow/HB2304/EK80/
Total objects: 1178
Total size: 224.26 GB
data/raw/Henry_B._Bigelow/HB2303/EK80/
Total objects: 11710
Total size: 2.25 TB
data/raw/Henry_B._Bigelow/HB2302/EK80/
Total objects: 1574
Total size: 153.74 GB
data/raw/Henry_B._Bigelow/HB2301/EK80/
Total objects: 835
Total size: 81.42 GB
data/raw/Henry_B._Bigelow/HB2206/EK60/
Total objects: 4044
Total size: 196.89 GB
data/raw/Pisces/PC2205/EK80/
Total objects: 1556
Total size: 564.09 GB
data/raw/Henry_B._Bigelow/HB2205/EK60/
Total objects: 1044
Total size: 48.73 GB
data/raw/Henry_B._Bigelow/HB2204/EK60/
Total objects: 1342
Total size: 65.11 GB
data/raw/Henry_B._Bigelow/HB2203/EK60/
Total objects: 282
Total size: 13.76 GB
data/raw/Henry_B._Bigelow/HB2202/EK60/
Total objects: 4596
Total size: 222.6 GB
data/raw/Henry_B._Bigelow/HB2103/EK60/
Total objects: 5428
Total size: 253.82 GB
data/raw/Henry_B._Bigelow/HB2102/EK60/
Total objects: 3484
Total size: 168.73 GB
data/raw/Pisces/PC2104/EK60/
Total objects: 1171
Total size: 55.07 GB
data/raw/Henry_B._Bigelow/HB2101/EK60/
Total objects: 14250
Total size: 695.33 GB
data/raw/Henry_B._Bigelow/HB2001/EK60/ # wip, aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB2001/EK60/ data/raw/Henry_B._Bigelow/HB2001/EK60/
Total objects: 1623
Total size: 52.01 GB
data/raw/Henry_B._Bigelow/HB1906/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1906/EK60/ data/raw/Henry_B._Bigelow/HB1906/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1906/metadata/ data/raw/Henry_B._Bigelow/HB1906/metadata/
Total objects: 5130
Total size: 167.16 GB
data/raw/Gordon_Gunter/GU1905/EK60/
Total objects: 1208
Total size: 118.0 GB
data/raw/Henry_B._Bigelow/HB1904/EK60/
Total objects: 672
Total size: 21.87 GB
data/raw/Henry_B._Bigelow/HB1907/EK60/
Total objects: 1755
Total size: 58.85 GB
data/raw/Henry_B._Bigelow/HB1903/EK60/
Total objects: 1095
Total size: 17.41 GB
data/raw/Henry_B._Bigelow/HB1902/EK60/
Total objects: 1656
Total size: 43.69 GB
data/raw/Henry_B._Bigelow/HB1901/EK60/
Total objects: 4497
Total size: 170.9 GB
data/raw/Henry_B._Bigelow/HB1806/EK60/
Total objects: 9561
Total size: 152.28 GB
data/raw/Henry_B._Bigelow/HB1805/EK60/
Total objects: 2028
Total size: 32.72 GB
data/raw/Henry_B._Bigelow/HB1803/EK60/
Total objects: 3957
Total size: 64.51 GB
data/raw/Henry_B._Bigelow/HB1802/EK60/
Total objects: 14571
Total size: 237.33 GB
data/raw/Henry_B._Bigelow/HB1801/EK60/
Total objects: 894
Total size: 14.55 GB
data/raw/Pisces/PC1706/EK60/
Total objects: 3111
Total size: 180.43 GB
data/raw/Henry_B._Bigelow/HB1702/EK60/
Total objects: 16032
Total size: 260.82 GB
data/raw/Henry_B._Bigelow/HB1701/EK60/
Total objects: 3927
Total size: 63.8 GB
data/raw/Henry_B._Bigelow/HB1604/EK60/
Total objects: 15957
Total size: 259.71 GB
data/raw/Pisces/PC1609/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Pisces/PC1609/EK60/ data/raw/Pisces/PC1609/EK60/
Total objects: 486
Total size: 7.95 GB
data/raw/Henry_B._Bigelow/HB1603/EK60/
Total objects: 9966
Total size: 155.59 GB
data/raw/Henry_B._Bigelow/HB1601/EK60/
Total objects: 6871
Total size: 112.21 GB
data/raw/Henry_B._Bigelow/HB1507/EK60/
Total objects: 1203
Total size: 19.59 GB
data/raw/Henry_B._Bigelow/HB1506/EK60/
Total objects: 12258
Total size: 199.93 GB
data/raw/Henry_B._Bigelow/HB1503/EK60/
Total objects: 2175
Total size: 35.06 GB
data/raw/Henry_B._Bigelow/HB1502/EK60/
Total objects: 2370
Total size: 33.25 GB
data/raw/Henry_B._Bigelow/HB1501/EK60/
Total objects: 11355
Total size: 185.02 GB
data/raw/Pisces/PC1405/EK60/
Total objects: 3207
Total size: 52.31 GB
data/raw/Henry_B._Bigelow/HB1405/EK60/
Total objects: 5631
Total size: 76.75 GB
data/raw/Pisces/PC1404/EK60/
# aws s3 sync s3://noaa-wcsd-pds/data/raw/Pisces/PC1404/EK60/ data/raw/Pisces/PC1404/EK60/
# done on pi
Total objects: 2265
Total size: 37.0 GB
data/raw/Henry_B._Bigelow/HB1403/EK60/
Total objects: 699
Total size: 22.39 GB
data/raw/Henry_B._Bigelow/HB1402/EK60/
# aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1402/EK60/ data/raw/Henry_B._Bigelow/HB1402/EK60/
Total objects: 528
Total size: 16.48 GB
data/raw/Henry_B._Bigelow/HB1401/EK60/
Total objects: 9123
Total size: 148.61 GB
data/raw/Gordon_Gunter/GU1402L1/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Gordon_Gunter/GU1402L1/EK60/ data/raw/Gordon_Gunter/GU1402L1/EK60/
    # done on pi
Total objects: 1821
Total size: 58.43 GB
data/raw/Gordon_Gunter/GU1402/GU1402L2/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Gordon_Gunter/GU1402/GU1402L2/EK60/ data/raw/Gordon_Gunter/GU1402/GU1402L2/EK60/
    # done on pi
Total objects: 2943
Total size: 95.82 GB
data/raw/Gordon_Gunter/GU1305/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Gordon_Gunter/GU1305/EK60/ data/raw/Gordon_Gunter/GU1305/EK60/
    # done on pi
Total objects: 2076
Total size: 33.69 GB
data/raw/Henry_B._Bigelow/HB1304/EK60/
Total objects: 15232
Total size: 175.33 GB
data/raw/Okeanos_Explorer/EX1305/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Okeanos_Explorer/EX1305/EK60/ data/raw/Okeanos_Explorer/EX1305/EK60/
Total objects: 810
Total size: 12.79 GB
data/raw/Henry_B._Bigelow/HB1303/EK60/
Total objects: 10314
Total size: 167.98 GB
data/raw/Henry_B._Bigelow/HB1301/EK60/
Total objects: 11145
Total size: 181.43 GB
data/raw/Pisces/PC1301/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Pisces/PC1301/EK60/ data/raw/Pisces/PC1301/EK60/
    # done on pi
Total objects: 3066
Total size: 49.63 GB
data/raw/Henry_B._Bigelow/HB1206/EK60/
Total objects: 12000
Total size: 195.35 GB
data/raw/Pisces/PC1206/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Pisces/PC1206/EK60/ data/raw/Pisces/PC1206/EK60/
    # done on pi
Total objects: 6264
Total size: 102.19 GB
data/raw/Henry_B._Bigelow/HB1201/EK60/
# aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1201/EK60/ data/raw/Henry_B._Bigelow/HB1201/EK60/
# done on pi, wip
Total objects: 12570
Total size: 204.86 GB
data/raw/Henry_B._Bigelow/HB1105/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1105/EK60/ data/raw/Henry_B._Bigelow/HB1105/EK60/
    # done on pi
Total objects: 10431
Total size: 169.84 GB
data/raw/Delaware_Ii/DE1108/EK60/
Total objects: 4281
Total size: 69.45 GB
data/raw/Henry_B._Bigelow/HB1103/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1103/EK60/ data/raw/Henry_B._Bigelow/HB1103/EK60/
    # done on pi
Total objects: 8325
Total size: 134.55 GB
data/raw/Henry_B._Bigelow/HB1102/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1102/EK60/ data/raw/Henry_B._Bigelow/HB1102/EK60/
    # done on pi
Total objects: 7103
Total size: 115.62 GB
data/raw/Delaware_Ii/DE1010/EK60/
Total objects: 3621
Total size: 58.43 GB
data/raw/Henry_B._Bigelow/HB1006/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1006/EK60/ data/raw/Henry_B._Bigelow/HB1006/EK60/
    # done on pi
Total objects: 5805
Total size: 93.65 GB
#
# left off here with metadata
#
data/raw/Delaware_Ii/DE0107/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0107/EK500/ data/raw/Delaware_Ii/DE0107/EK500/
Total objects: 894
Total size: 1.67 GB
data/raw/Henry_B._Bigelow/HB1002/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB1002/EK60/ data/raw/Henry_B._Bigelow/HB1002/EK60/
    # done on pi, wip
Total objects: 11491
Total size: 187.09 GB
data/raw/Henry_B._Bigelow/HB0905/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0905/EK60/ data/raw/Henry_B._Bigelow/HB0905/EK60/
Total objects: 5883
Total size: 95.58 GB
data/raw/Delaware_Ii/DE0910/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0910/EK60/ data/raw/Delaware_Ii/DE0910/EK60/
Total objects: 3597
Total size: 58.57 GB
data/raw/Henry_B._Bigelow/HB0904/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0904/EK60 data/raw/Henry_B._Bigelow/HB0904/EK60
Total objects: 1851
Total size: 6.05 GB
data/raw/Henry_B._Bigelow/HB0903/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0903/EK60/ data/raw/Henry_B._Bigelow/HB0903/EK60/
Total objects: 663
Total size: 7.47 GB
data/raw/Henry_B._Bigelow/HB0902/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0902/EK60/ data/raw/Henry_B._Bigelow/HB0902/EK60/
Total objects: 3663
Total size: 54.36 GB
data/raw/Henry_B._Bigelow/HB0901/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0901/EK60/ data/raw/Henry_B._Bigelow/HB0901/EK60/
Total objects: 10320
Total size: 167.97 GB
data/raw/Henry_B._Bigelow/HB0807/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0807/EK60/ data/raw/Henry_B._Bigelow/HB0807/EK60/
Total objects: 10572
Total size: 171.95 GB
data/raw/Albatross_Iv/AL0803/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0803/EK60/ data/raw/Albatross_Iv/AL0803/EK60/
Total objects: 8389
Total size: 54.68 GB
data/raw/Delaware_Ii/DE0809/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0809/EK500/ data/raw/Delaware_Ii/DE0809/EK500/
Total objects: 2411
Total size: 4.6 GB
data/raw/Henry_B._Bigelow/HB0806/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0806/EK60/ data/raw/Henry_B._Bigelow/HB0806/EK60/
Total objects: 369
Total size: 12.8 GB
data/raw/Henry_B._Bigelow/HB0805/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0805/EK60/ data/raw/Henry_B._Bigelow/HB0805/EK60/
Total objects: 1731
Total size: 11.1 GB
data/raw/Henry_B._Bigelow/HB0803/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0803/EK60/ data/raw/Henry_B._Bigelow/HB0803/EK60/
Total objects: 5466
Total size: 35.6 GB
data/raw/Albatross_Iv/AL0801/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0801/EK60/ data/raw/Albatross_Iv/AL0801/EK60/
Total objects: 2391
Total size: 70.39 GB
data/raw/Henry_B._Bigelow/HB0802/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0802/EK60/ data/raw/Henry_B._Bigelow/HB0802/EK60/
Total objects: 17388
Total size: 113.32 GB
data/raw/Henry_B._Bigelow/HB0711/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0711/EK60/ data/raw/Henry_B._Bigelow/HB0711/EK60/
Total objects: 648
Total size: 25.56 GB
data/raw/Delaware_Ii/DE0710/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0710/EK500/ data/raw/Delaware_Ii/DE0710/EK500/
Total objects: 1494
Total size: 3.03 GB
data/raw/Henry_B._Bigelow/HB0710/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0710/EK60/ data/raw/Henry_B._Bigelow/HB0710/EK60/
Total objects: 129
Total size: 7.97 GB
data/raw/Henry_B._Bigelow/HB0706/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0706/EK60/ data/raw/Henry_B._Bigelow/HB0706/EK60/
Total objects: 159
Total size: 9.6 GB
data/raw/Henry_B._Bigelow/HB0707/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0707/EK60/ data/raw/Henry_B._Bigelow/HB0707/EK60/
Total objects: 36
Total size: 1.91 GB
data/raw/Delaware_Ii/DE0615/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0615/EK500/ data/raw/Delaware_Ii/DE0615/EK500/
Total objects: 2217
Total size: 4.22 GB
data/raw/Albatross_Iv/AL0509/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0509/EK60/ data/raw/Albatross_Iv/AL0509/EK60/
Total objects: 382
Total size: 3.68 GB
data/raw/Albatross_Iv/AL0508/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0508/EK60/ data/raw/Albatross_Iv/AL0508/EK60/
Total objects: 1493
Total size: 14.51 GB
data/raw/Delaware_Ii/DE0512/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0512/EK500/ data/raw/Delaware_Ii/DE0512/EK500/
Total objects: 2359
Total size: 4.52 GB
data/raw/Delaware_Ii/DE0505/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0505/EK500/ data/raw/Delaware_Ii/DE0505/EK500/
Total objects: 329
Total size: 6.36 GB
data/raw/Albatross_Iv/AL0504/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0504/EK60/ data/raw/Albatross_Iv/AL0504/EK60/
Total objects: 271
Total size: 2.64 GB
data/raw/Albatross_Iv/AL0502/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0502/EK60/ data/raw/Albatross_Iv/AL0502/EK60/
Total objects: 662
Total size: 6.46 GB
data/raw/Albatross_Iv/AL0409/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0409/EK60/ data/raw/Albatross_Iv/AL0409/EK60/
Total objects: 2198
Total size: 32.65 GB
data/raw/Delaware_Ii/DE0413/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0413/EK500/ data/raw/Delaware_Ii/DE0413/EK500/
Total objects: 2160
Total size: 21.17 GB
data/raw/Delaware_Ii/DE0410/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0410/EK500/ data/raw/Delaware_Ii/DE0410/EK500/
Total objects: 268
Total size: 1.05 GB
data/raw/Delaware_Ii/DE0408/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0408/EK500/ data/raw/Delaware_Ii/DE0408/EK500/
Total objects: 1837
Total size: 7.21 GB
data/raw/Albatross_Iv/AL0404/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0404/EK60/ data/raw/Albatross_Iv/AL0404/EK60/
Total objects: 50
Total size: 4.58 GB
data/raw/Albatross_Iv/AL0403/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0403/EK60/ data/raw/Albatross_Iv/AL0403/EK60/
Total objects: 145
Total size: 13.06 GB
data/raw/Albatross_Iv/AL0401/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0401/EK60/ data/raw/Albatross_Iv/AL0401/EK60/
Total objects: 1114
Total size: 4.37 GB
data/raw/Albatross_Iv/AL0305/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0305/EK60/ data/raw/Albatross_Iv/AL0305/EK60/
Total objects: 7010
Total size: 27.47 GB
data/raw/Albatross_Iv/AL0304/EK60/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0304/EK60/ data/raw/Albatross_Iv/AL0304/EK60/
Total objects: 620
Total size: 2.42 GB
data/raw/Delaware_Ii/DE0306/EK500/
    #aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0306/EK500/ data/raw/Delaware_Ii/DE0306/EK500/
Total objects: 182
Total size: 722.08 MB
data/raw/Delaware_Ii/DE0303/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0303/EK500/ data/raw/Delaware_Ii/DE0303/EK500/
Total objects: 1807
Total size: 7.05 GB
data/raw/Delaware_Ii/DE0302/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0302/EK500/ data/raw/Delaware_Ii/DE0302/EK500/
Total objects: 868
Total size: 3.38 GB
data/raw/Delaware_Ii/DE0301/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0301/EK500/ data/raw/Delaware_Ii/DE0301/EK500/
Total objects: 334
Total size: 1.3 GB
data/raw/Albatross_Iv/AL0210/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0210/EK500/ data/raw/Albatross_Iv/AL0210/EK500/
Total objects: 358
Total size: 1.32 GB
data/raw/Delaware_Ii/DE0208/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0208/EK500/ data/raw/Delaware_Ii/DE0208/EK500/
Total objects: 1128
Total size: 4.38 GB
data/raw/Delaware_Ii/DE0206/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0206/EK500/ data/raw/Delaware_Ii/DE0206/EK500/
Total objects: 112
Total size: 405.55 MB
data/raw/Albatross_Iv/AL0207/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0207/EK500/ data/raw/Albatross_Iv/AL0207/EK500/
Total objects: 210
Total size: 804.11 MB
data/raw/Albatross_Iv/AL0204/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0204/EK500/ data/raw/Albatross_Iv/AL0204/EK500/
Total objects: 706
Total size: 2.64 GB
data/raw/Delaware_Ii/DE0201/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0201/EK500/ data/raw/Delaware_Ii/DE0201/EK500/
Total objects: 509
Total size: 1.96 GB
data/raw/Albatross_Iv/AL0203/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0203/EK500/ data/raw/Albatross_Iv/AL0203/EK500/
Total objects: 409
Total size: 1.54 GB
data/raw/Albatross_Iv/AL0110/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0110/EK500/ data/raw/Albatross_Iv/AL0110/EK500/
Total objects: 881
Total size: 2.68 GB
data/raw/Delaware_Ii/DE0109/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0109/EK500/ data/raw/Delaware_Ii/DE0109/EK500/
Total objects: 1136
Total size: 4.22 GB
data/raw/Delaware_Ii/DE0108/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0108/EK500/ data/raw/Delaware_Ii/DE0108/EK500/
Total objects: 1481
Total size: 2.82 GB
data/raw/Albatross_Iv/AL0105/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0105/EK500/ data/raw/Albatross_Iv/AL0105/EK500/
Total objects: 4846
Total size: 1.51 GB
data/raw/Albatross_Iv/AL0104/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0104/EK500/ data/raw/Albatross_Iv/AL0104/EK500/
Total objects: 687
Total size: 339.61 MB
data/raw/Albatross_Iv/AL0103/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0103/EK500/ data/raw/Albatross_Iv/AL0103/EK500/
Total objects: 10664
Total size: 4.55 GB
data/raw/Albatross_Iv/AL0102/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0102/EK500/ data/raw/Albatross_Iv/AL0102/EK500/
Total objects: 4800
Total size: 2.26 GB
data/raw/Delaware_Ii/DE0101/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0101/EK500/ data/raw/Delaware_Ii/DE0101/EK500/
Total objects: 7594
Total size: 1.85 GB
data/raw/Albatross_Iv/AL0007/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0007/EK500/ data/raw/Albatross_Iv/AL0007/EK500/
Total objects: 4992
Total size: 1.64 GB
data/raw/Albatross_Iv/AL0006/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0006/EK500/ data/raw/Albatross_Iv/AL0006/EK500/
Total objects: 6494
Total size: 2.87 GB
data/raw/Delaware_Ii/DE0008/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0008/EK500/ data/raw/Delaware_Ii/DE0008/EK500/
Total objects: 17765
Total size: 4.43 GB
data/raw/Delaware_Ii/DE0007/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0007/EK500/ data/raw/Delaware_Ii/DE0007/EK500/
Total objects: 1885
Total size: 847.98 MB
data/raw/Delaware_Ii/DE0005/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0005/EK500/ data/raw/Delaware_Ii/DE0005/EK500/
Total objects: 15081
Total size: 5.64 GB
data/raw/Albatross_Iv/AL0002/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0002/EK500/ data/raw/Albatross_Iv/AL0002/EK500/
Total objects: 10038
Total size: 4.4 GB
data/raw/Albatross_Iv/AL0001/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0001/EK500/ data/raw/Albatross_Iv/AL0001/EK500/
Total objects: 4024
Total size: 1.81 GB
data/raw/Delaware_Ii/DE0002/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0002/EK500/ data/raw/Delaware_Ii/DE0002/EK500/
Total objects: 1226
Total size: 330.38 MB
data/raw/Albatross_Iv/AL9911/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9911/EK500/ data/raw/Albatross_Iv/AL9911/EK500/
Total objects: 9848
Total size: 4.51 GB
data/raw/Delaware_Ii/DE9909/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9909/EK500/ data/raw/Delaware_Ii/DE9909/EK500/
Total objects: 16192
Total size: 3.78 GB
data/raw/Delaware_Ii/DE9908/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9908/EK500/ data/raw/Delaware_Ii/DE9908/EK500/
Total objects: 6147
Total size: 2.34 GB
data/raw/Delaware_Ii/DE9906/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9906/EK500/ data/raw/Delaware_Ii/DE9906/EK500/
Total objects: 413
Total size: 114.05 MB
data/raw/Albatross_Iv/AL9903/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9903/EK500/ data/raw/Albatross_Iv/AL9903/EK500/
Total objects: 10297
Total size: 4.5 GB
data/raw/Delaware_Ii/DE9903/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9903/EK500/ data/raw/Delaware_Ii/DE9903/EK500/
Total objects: 1116
Total size: 327.36 MB
data/raw/Albatross_Iv/AL9902/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9902/EK500/ data/raw/Albatross_Iv/AL9902/EK500/
Total objects: 4359
Total size: 2.12 GB
data/raw/Albatross_Iv/AL9811/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9811/EK500/ data/raw/Albatross_Iv/AL9811/EK500/
Total objects: 81
Total size: 1.9 GB
data/raw/Delaware_Ii/DE9810/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9810/EK500/ data/raw/Delaware_Ii/DE9810/EK500/
Total objects: 12564
Total size: 2.61 GB
data/raw/Delaware_Ii/DE9809/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9809/EK500/ data/raw/Delaware_Ii/DE9809/EK500/
Total objects: 2097
Total size: 488.07 MB
data/raw/Albatross_Iv/AL9804/EK500/
    # aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9804/EK500/ data/raw/Albatross_Iv/AL9804/EK500/
Total objects: 37
Total size: 698.21 MB
```
For a grand total of:
```commandline
Total objects: 616527
Total size: 12.9 TB
```

To tar a file
> tar -czvf noaa-dcdb-bathymetry-pds-index.tar.gz noaa-dcdb-bathymetry-pds-index.csv
And then
```commandline
$ sha256sum noaa-dcdb-bathymetry-pds-index.tar.gz
3f1cbc3831ca133061a53c9a4bc949987a8e6191d2fa78a943011c0bfcd595d9  noaa-dcdb-bathymetry-pds-index.tar.gz
```

























aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0107/EK500/ data/raw/Delaware_Ii/DE0107/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0905/EK60/ data/raw/Henry_B._Bigelow/HB0905/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0910/EK60/ data/raw/Delaware_Ii/DE0910/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0904/EK60 data/raw/Henry_B._Bigelow/HB0904/EK60
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0903/EK60/ data/raw/Henry_B._Bigelow/HB0903/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0902/EK60/ data/raw/Henry_B._Bigelow/HB0902/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0901/EK60/ data/raw/Henry_B._Bigelow/HB0901/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0807/EK60/ data/raw/Henry_B._Bigelow/HB0807/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0803/EK60/ data/raw/Albatross_Iv/AL0803/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0809/EK500/ data/raw/Delaware_Ii/DE0809/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0806/EK60/ data/raw/Henry_B._Bigelow/HB0806/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0805/EK60/ data/raw/Henry_B._Bigelow/HB0805/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0803/EK60/ data/raw/Henry_B._Bigelow/HB0803/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0801/EK60/ data/raw/Albatross_Iv/AL0801/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0802/EK60/ data/raw/Henry_B._Bigelow/HB0802/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0711/EK60/ data/raw/Henry_B._Bigelow/HB0711/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0710/EK500/ data/raw/Delaware_Ii/DE0710/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0710/EK60/ data/raw/Henry_B._Bigelow/HB0710/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0706/EK60/ data/raw/Henry_B._Bigelow/HB0706/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0707/EK60/ data/raw/Henry_B._Bigelow/HB0707/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0615/EK500/ data/raw/Delaware_Ii/DE0615/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0509/EK60/ data/raw/Albatross_Iv/AL0509/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0508/EK60/ data/raw/Albatross_Iv/AL0508/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0512/EK500/ data/raw/Delaware_Ii/DE0512/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0505/EK500/ data/raw/Delaware_Ii/DE0505/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0504/EK60/ data/raw/Albatross_Iv/AL0504/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0502/EK60/ data/raw/Albatross_Iv/AL0502/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0409/EK60/ data/raw/Albatross_Iv/AL0409/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0413/EK500/ data/raw/Delaware_Ii/DE0413/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0410/EK500/ data/raw/Delaware_Ii/DE0410/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0408/EK500/ data/raw/Delaware_Ii/DE0408/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0404/EK60/ data/raw/Albatross_Iv/AL0404/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0403/EK60/ data/raw/Albatross_Iv/AL0403/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0401/EK60/ data/raw/Albatross_Iv/AL0401/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0305/EK60/ data/raw/Albatross_Iv/AL0305/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0304/EK60/ data/raw/Albatross_Iv/AL0304/EK60/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0306/EK500/ data/raw/Delaware_Ii/DE0306/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0303/EK500/ data/raw/Delaware_Ii/DE0303/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0302/EK500/ data/raw/Delaware_Ii/DE0302/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0301/EK500/ data/raw/Delaware_Ii/DE0301/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0210/EK500/ data/raw/Albatross_Iv/AL0210/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0208/EK500/ data/raw/Delaware_Ii/DE0208/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0206/EK500/ data/raw/Delaware_Ii/DE0206/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0207/EK500/ data/raw/Albatross_Iv/AL0207/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0204/EK500/ data/raw/Albatross_Iv/AL0204/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0201/EK500/ data/raw/Delaware_Ii/DE0201/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0203/EK500/ data/raw/Albatross_Iv/AL0203/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0110/EK500/ data/raw/Albatross_Iv/AL0110/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0109/EK500/ data/raw/Delaware_Ii/DE0109/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0108/EK500/ data/raw/Delaware_Ii/DE0108/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0105/EK500/ data/raw/Albatross_Iv/AL0105/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0104/EK500/ data/raw/Albatross_Iv/AL0104/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0103/EK500/ data/raw/Albatross_Iv/AL0103/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0102/EK500/ data/raw/Albatross_Iv/AL0102/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0101/EK500/ data/raw/Delaware_Ii/DE0101/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0007/EK500/ data/raw/Albatross_Iv/AL0007/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0006/EK500/ data/raw/Albatross_Iv/AL0006/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0008/EK500/ data/raw/Delaware_Ii/DE0008/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0007/EK500/ data/raw/Delaware_Ii/DE0007/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0005/EK500/ data/raw/Delaware_Ii/DE0005/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0002/EK500/ data/raw/Albatross_Iv/AL0002/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0001/EK500/ data/raw/Albatross_Iv/AL0001/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0002/EK500/ data/raw/Delaware_Ii/DE0002/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9911/EK500/ data/raw/Albatross_Iv/AL9911/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9909/EK500/ data/raw/Delaware_Ii/DE9909/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9908/EK500/ data/raw/Delaware_Ii/DE9908/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9906/EK500/ data/raw/Delaware_Ii/DE9906/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9903/EK500/ data/raw/Albatross_Iv/AL9903/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9903/EK500/ data/raw/Delaware_Ii/DE9903/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9902/EK500/ data/raw/Albatross_Iv/AL9902/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9811/EK500/ data/raw/Albatross_Iv/AL9811/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9810/EK500/ data/raw/Delaware_Ii/DE9810/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9809/EK500/ data/raw/Delaware_Ii/DE9809/EK500/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9804/EK500/ data/raw/Albatross_Iv/AL9804/EK500/

# metadata
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0107/metadata/ data/raw/Delaware_Ii/DE0107/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0905/metadata/ data/raw/Henry_B._Bigelow/HB0905/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0910/metadata/ data/raw/Delaware_Ii/DE0910/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0904/metadata data/raw/Henry_B._Bigelow/HB0904/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0903/metadata/ data/raw/Henry_B._Bigelow/HB0903/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0902/metadata/ data/raw/Henry_B._Bigelow/HB0902/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0901/metadata/ data/raw/Henry_B._Bigelow/HB0901/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0807/metadata/ data/raw/Henry_B._Bigelow/HB0807/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0803/metadata/ data/raw/Albatross_Iv/AL0803/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0809/metadata/ data/raw/Delaware_Ii/DE0809/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0806/metadata/ data/raw/Henry_B._Bigelow/HB0806/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0805/metadata/ data/raw/Henry_B._Bigelow/HB0805/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0803/metadata/ data/raw/Henry_B._Bigelow/HB0803/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0801/metadata/ data/raw/Albatross_Iv/AL0801/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0802/metadata/ data/raw/Henry_B._Bigelow/HB0802/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0711/metadata/ data/raw/Henry_B._Bigelow/HB0711/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0710/metadata/ data/raw/Delaware_Ii/DE0710/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0710/metadata/ data/raw/Henry_B._Bigelow/HB0710/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0706/metadata/ data/raw/Henry_B._Bigelow/HB0706/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Henry_B._Bigelow/HB0707/metadata/ data/raw/Henry_B._Bigelow/HB0707/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0615/metadata/ data/raw/Delaware_Ii/DE0615/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0509/metadata/ data/raw/Albatross_Iv/AL0509/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0508/metadata/ data/raw/Albatross_Iv/AL0508/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0512/metadata/ data/raw/Delaware_Ii/DE0512/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0505/metadata/ data/raw/Delaware_Ii/DE0505/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0504/metadata/ data/raw/Albatross_Iv/AL0504/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0502/metadata/ data/raw/Albatross_Iv/AL0502/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0409/metadata/ data/raw/Albatross_Iv/AL0409/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0413/metadata/ data/raw/Delaware_Ii/DE0413/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0410/metadata/ data/raw/Delaware_Ii/DE0410/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0408/metadata/ data/raw/Delaware_Ii/DE0408/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0404/metadata/ data/raw/Albatross_Iv/AL0404/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0403/metadata/ data/raw/Albatross_Iv/AL0403/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0401/metadata/ data/raw/Albatross_Iv/AL0401/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0305/metadata/ data/raw/Albatross_Iv/AL0305/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0304/metadata/ data/raw/Albatross_Iv/AL0304/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0306/metadata/ data/raw/Delaware_Ii/DE0306/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0303/metadata/ data/raw/Delaware_Ii/DE0303/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0302/metadata/ data/raw/Delaware_Ii/DE0302/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0301/metadata/ data/raw/Delaware_Ii/DE0301/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0210/metadata/ data/raw/Albatross_Iv/AL0210/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0208/metadata/ data/raw/Delaware_Ii/DE0208/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0206/metadata/ data/raw/Delaware_Ii/DE0206/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0207/metadata/ data/raw/Albatross_Iv/AL0207/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0204/metadata/ data/raw/Albatross_Iv/AL0204/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0201/metadata/ data/raw/Delaware_Ii/DE0201/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0203/metadata/ data/raw/Albatross_Iv/AL0203/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0110/metadata/ data/raw/Albatross_Iv/AL0110/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0109/metadata/ data/raw/Delaware_Ii/DE0109/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0108/metadata/ data/raw/Delaware_Ii/DE0108/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0105/metadata/ data/raw/Albatross_Iv/AL0105/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0104/metadata/ data/raw/Albatross_Iv/AL0104/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0103/metadata/ data/raw/Albatross_Iv/AL0103/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0102/metadata/ data/raw/Albatross_Iv/AL0102/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0101/metadata/ data/raw/Delaware_Ii/DE0101/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0007/metadata/ data/raw/Albatross_Iv/AL0007/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0006/metadata/ data/raw/Albatross_Iv/AL0006/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0008/metadata/ data/raw/Delaware_Ii/DE0008/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0007/metadata/ data/raw/Delaware_Ii/DE0007/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0005/metadata/ data/raw/Delaware_Ii/DE0005/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0002/metadata/ data/raw/Albatross_Iv/AL0002/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL0001/metadata/ data/raw/Albatross_Iv/AL0001/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE0002/metadata/ data/raw/Delaware_Ii/DE0002/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9911/metadata/ data/raw/Albatross_Iv/AL9911/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9909/metadata/ data/raw/Delaware_Ii/DE9909/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9908/metadata/ data/raw/Delaware_Ii/DE9908/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9906/metadata/ data/raw/Delaware_Ii/DE9906/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9903/metadata/ data/raw/Albatross_Iv/AL9903/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9903/metadata/ data/raw/Delaware_Ii/DE9903/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9902/metadata/ data/raw/Albatross_Iv/AL9902/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9811/metadata/ data/raw/Albatross_Iv/AL9811/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9810/metadata/ data/raw/Delaware_Ii/DE9810/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Delaware_Ii/DE9809/metadata/ data/raw/Delaware_Ii/DE9809/metadata/
aws s3 sync s3://noaa-wcsd-pds/data/raw/Albatross_Iv/AL9804/metadata/ data/raw/Albatross_Iv/AL9804/metadata/


# Google Bucket Info
DESKTOP:/mnt/c/Users/user$ gsutil du -s gs://noaa-passive-bioacoustic/
292918473535088  gs://noaa-passive-bioacoustic
DESKTOP:/mnt/c/Users/user$
