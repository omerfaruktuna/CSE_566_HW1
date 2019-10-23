import numpy as np

with open('input_data.txt', 'r') as f:
  dataset = []
  content = f.readlines()
  x = 0
  for line in content:
    if x == 0:
      number_of_lines = int(line.strip())
      x+=1
      continue

    dataset.append([])
    for i in range(len(line.strip().split(" "))):
      dataset[x-1].append(float(line.strip().split(" ")[i]))
    x+=1


features = np.array(dataset)[:,:-1]
labels = np.array(dataset)[:,-1]


def make_rectangle(vector_2d):

  rect = []
  rect.append(vector_2d[0])
  rect.append(vector_2d[0])
  rect.append(vector_2d[1])
  rect.append(vector_2d[1])

  return rect


def is_in_rectangle(vector_2d,rectangle):

  if vector_2d[0]>=rectangle[0] and vector_2d[0]<=rectangle[1] and vector_2d[1]>=rectangle[2] and vector_2d[1]<=rectangle[3]:
    return True
  else:
    return False


def enlarge_coordinates(vector_2d,rectangle):

    tmp = rectangle.copy()

    if vector_2d[0]<tmp[0]:
      tmp[0] = vector_2d[0]

    if vector_2d[0]>tmp[1]:
      tmp[1] = vector_2d[0]

    if vector_2d[1]<tmp[2]:
      tmp[2] = vector_2d[1]

    if vector_2d[1]>tmp[3]:
      tmp[3] = vector_2d[1]

    return tmp

def shrink_coordinates(vector_2d,rectangle):

    tmp = rectangle.copy()

    if vector_2d[0]>tmp[0]:
      tmp[0] = vector_2d[0]

    if vector_2d[0]<tmp[1]:
      tmp[1] = vector_2d[0]

    if vector_2d[1]>tmp[2]:
      tmp[2] = vector_2d[1]

    if vector_2d[1]<tmp[3]:
      tmp[3] = vector_2d[1]

    return tmp

def is_including(rect_1,rect_2):
  if rect_1[0] <= rect_2[0] and rect_1[1]>=rect_2[1] and rect_1[2]<= rect_2[2] and rect_1[3]>=rect_2[3]:
    return True
  else:
    return False

def most_specific(feature,label):
    for i,val in enumerate(label):
        if val== 1:
            first_hypothesis = feature[i].copy()
            break

    rectangle_coords = make_rectangle(first_hypothesis)

    for i,val in enumerate(feature):
        if label[i] == 1:

            if not is_in_rectangle(val,rectangle_coords):
              rectangle_coords = enlarge_coordinates(val,rectangle_coords)

    return rectangle_coords

most_specific_hypothesis_coordinates = most_specific(features,labels)
print('\nCoordinates of rectange describing most specific hypothesis based on input data is: ')
print(most_specific_hypothesis_coordinates)
print('\n')


def most_general(feature,label,most_specific_hypothesis):

    rectangle_coords = most_specific_hypothesis

    for i,val in enumerate(label):
        if val == 0:
          #print("###")
          #print(rectangle_coords)
          if not is_in_rectangle(feature[i],rectangle_coords):
            first_hypothesis = feature[i].copy()
            #print(first_hypothesis)
            break

    rectangle_coords = enlarge_coordinates(first_hypothesis,rectangle_coords)


    for i,val in enumerate(feature):
        if label[i] == 0:
          if is_in_rectangle(val,rectangle_coords):
            rectangle_coords = enlarge_coordinates(val,most_specific_hypothesis)

    return rectangle_coords

most_general_hypothesis_coordinates = most_general(features,labels,most_specific_hypothesis_coordinates)
print('\nCoordinates of rectange describing most general hypothesis based on input data is: ')
print(most_general_hypothesis_coordinates)
print('\n')
