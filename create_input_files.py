from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='/dlwsdata2/public/coco/annotations/dataset_coco.json',
                       image_folder='/dlwsdata2/public/coco/images/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/dlwsdata2/public/coco/output/',
                       max_len=50)
