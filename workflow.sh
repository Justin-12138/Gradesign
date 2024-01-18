echo "开始去除颅骨"
input_dir="data"
brain_struc="brain_struc"
mkdir -p $brain_struc
for file in $input_dir/*.nii
do
  base_name=$(basename $file .nii)
  output_file="$brain_struc/${base_name}.nii.gz"
  bet2 $file $output_file -f 0.5
  echo "$file 颅骨去除完成"
done
echo "颅骨去除完毕!"
echo "--------------------------------------------------------------"
echo "开始配准"
template="template152"
mkdir -p $template
mni152_template="/usr/local/fsl/data/standard/MNI152_T1_1mm.nii.gz"

for file in $brain_struc/*.nii.gz
do
  base_name=$(basename $file .nii.gz)
  flirt -in $file -ref $mni152_template -out "$template/${base_name}.nii.gz"
  echo "$file 配准完成"
done
echo "配准完毕!"
echo "--------------------------------------------------------------"
echo "开始平滑"
gauss="Gauss_smooth"
mkdir -p $gauss

for file in $template/*.nii.gz
do
  base_name=$(basename $file .nii.gz)
  fslmaths $file -s 2 "$gauss/${base_name}.nii.gz"
  echo "$file 平滑完成"
done
echo "平滑完毕!"

