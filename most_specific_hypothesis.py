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


def update_coordinates(vector_2d,rectangle):

    if vector_2d[0]<rectangle[0]:
      rectangle[0] = vector_2d[0]

    if vector_2d[0]>rectangle[1]:
      rectangle[1] = vector_2d[0]

    if vector_2d[1]<rectangle[2]:
      rectangle[2] = vector_2d[1]

    if vector_2d[1]>rectangle[3]:
      rectangle[3] = vector_2d[1]

    return rectangle

def most_specific(feature,label):
    for i,val in enumerate(label):
        if val== 1:
            first_hypothesis = feature[i].copy()
            break

    rectangle_coords = make_rectangle(first_hypothesis)

            
    for i,val in enumerate(feature):
        if label[i] == 1:

            if not is_in_rectangle(val,rectangle_coords):
              rectangle_coords = update_coordinates(val,rectangle_coords)

    return rectangle_coords

print('Coordinates of rectange describing most specific hypothesis based on input data is: ')
print(most_specific(features,labels))

