from osgeo import ogr

# Test filename to work with in the meantime
filename = '/Users/jacaraba/Desktop/development/ilab/nccs-remote-sensing-work/data/MOD44B.A2016065.h14v10.006.2017081141243.hdf'

modis_template_layers = 'HDF4_EOS:EOS_GRID:"%s":MOD44B_250m_GRID:%s'  # template from MODIS product
modis_selected_layers = ['Percent_Tree_Cover']  # modis layers to utilize
data = dict()  # dictionary to store retrieved data

for i, layer in enumerate ( modis_selected_layers ):
    read_file = modis_template_layers % ( filename, layer )
    print ("Opening Layer %d: %s" % (i+1, read_file ))
    g = gdal.Open(read_file)
    assert g is not None, f"Problem opening file {read_file}"

    data[layer] = g.ReadAsArray()
    print ("\t>>> Read %s!" % layer)

from rioxarray.merge import merge_datasets
merged = merge_datasets(datasets_list)
