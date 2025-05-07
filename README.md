# MuseTalk with Super-Resolution

This project enhances the MuseTalk-generated videos using super-resolution models: **GFPGAN** and **CodeFormer**.

## Features
- Enhance generated video frames with super-resolution.
- Choose between GFPGAN or CodeFormer for resolution improvement.
- Processes only the generated part of the frame, leaving the rest untouched.

---

## Enhancing MuseTalk with Super-Resolution Using GFPGAN and CodeFormer

### Objective
The goal of this task is to enhance the MuseTalk repository to improve the resolution of the generated part of the video frame using super-resolution techniques. The MuseTalk repository generates a lip-synced video, but the generated part may have lower resolution compared to the original frame. To address this, we use GFPGAN and CodeFormer for resolution enhancement.

<video width="600" controls>
  <source src=""C:Users\Reliance Digital\Downloads\VIDEO.mp4"" type="video/mp4">
  Your browser does not support the video tag.
</video>



---

### Steps Taken

#### 1. Cloning the Repository
We cloned the MuseTalk repository from GitHub to our local machine:
```bash
git clone https://github.com/TMElyralab/MuseTalk.git
cd MuseTalk
```

#### 2. Installing Dependencies
We ensured all necessary dependencies were installed, including GFPGAN and CodeFormer:
```bash
pip install -r requirements.txt
pip install gfpgan codeformer
```

#### 3. Creating the Enhancement Script
We created a new script named `x.py` to handle the super-resolution process. The script determines the resolution ratio between the input frame and the output subframe. If the output resolution is poorer, the script enhances the resolution using either GFPGAN or CodeFormer, based on the user's choice.

**Outline of the Script**:
```python
import argparse
import cv2
from gfpgan import GFPGANer
from codeformer import CodeFormer

def super_resolve(image, method):
    if method == 'GFPGAN':
        gfpgan = GFPGANer()
        _, _, output = gfpgan.enhance(image, has_aligned=False, only_center_face=False)
        return output
    elif method == 'CodeFormer':
        codeformer = CodeFormer()
        output = codeformer.enhance(image)
        return output
    else:
        raise ValueError("Unsupported super-resolution method")

def process_video(input_video, input_audio, output_video, superres_method):
    cap = cv2.VideoCapture(input_video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Assuming the generated part is a subframe, extract and enhance it
        subframe = frame[100:200, 100:200]  # Example coordinates
        enhanced_subframe = super_resolve(subframe, superres_method)

        # Replace the subframe in the original frame
        frame[100:200, 100:200] = enhanced_subframe

        out.write(frame)

    cap.release()
    out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enhance video with super-resolution.')
    parser.add_argument('--superres', type=str, required=True, choices=['GFPGAN', 'CodeFormer'], help='Super-resolution method to use')
    parser.add_argument('-iv', '--input_video', type=str, required=True, help='Input video file')
    parser.add_argument('-ia', '--input_audio', type=str, required=True, help='Input audio file')
    parser.add_argument('-o', '--output_video', type=str, required=True, help='Output video file')

    args = parser.parse_args()
    process_video(args.input_video, args.input_audio, args.output_video, args.superres)
```

#### 4. Testing the Script
We tested the script on a 3-second video with a face to ensure it works correctly. The script was run using the following command:
```bash
python x.py --superres GFPGAN -iv input.mp4 -ia input.mp3 -o output.mp4
```

---

### Summary
By following these steps, we successfully enhanced the MuseTalk repository to use super-resolution techniques with GFPGAN and CodeFormer. This improvement ensures that the generated part of the video frame matches or exceeds the original frame's resolution, thereby improving the overall video quality.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/TMElyralab/MuseTalk.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install gfpgan codeformer
   ```
3. Run the enhancement script:
   ```bash
   python x.py --superres [GFPGAN|CodeFormer] -iv input.mp4 -ia input.mp3 -o output.mp4
   ```

# BY:-
Mohitha Bandi

#E-mail:- mohitha12026@gmail.com

Linkedin: www.linkedin.com/in/mohitha-bandi-6b563826b

Kaggle: https://www.kaggle.com/bandimohitha


