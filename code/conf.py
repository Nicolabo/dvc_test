import os

data_dir = 'data'

source_xml = os.path.join(data_dir, 'xml/Posts.xml')
source_tsv = os.path.join(data_dir, 'tsv/Posts.tsv')

train_tsv = os.path.join(data_dir, 'tt/Posts-train.tsv')
test_tsv = os.path.join(data_dir, 'tt/Posts-test.tsv')

train_matrix = os.path.join(data_dir, 'matrix_t/matrix-train.p')
test_matrix = os.path.join(data_dir, 'matrix_t/matrix-test.p')

model = os.path.join(data_dir, 'model/model.p')

