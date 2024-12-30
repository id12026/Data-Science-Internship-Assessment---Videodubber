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
        raise ValueError("Unsupported superresolution method")

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
    parser = argparse.ArgumentParser(description='Enhance video with superresolution.')
    parser.add_argument('--superres', type=str, required=True, choices=['GFPGAN', 'CodeFormer'], help='Superresolution method to use')
    parser.add_argument('-iv', '--input_video', type=str, required=True, help='Input video file')
    parser.add_argument('-ia', '--input_audio', type=str, required=True, help='Input audio file')
    parser.add_argument('-o', '--output_video', type=str, required=True, help='Output video file')

    args = parser.parse_args()
    process_video(args.input_video, args.input_audio, args.output_video, args.superres)