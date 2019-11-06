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

    if vector_2d[0]<=tmp[0]:
      tmp[0] = vector_2d[0]

    if vector_2d[0]>=tmp[1]:
      tmp[1] = vector_2d[0]

    if vector_2d[1]<=tmp[2]:
      tmp[2] = vector_2d[1]

    if vector_2d[1]>=tmp[3]:
      tmp[3] = vector_2d[1]

    return tmp

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
print('\nCoordinates of rectangle (x1,x2,y1,y2) describing Most Specific Hypothesis S based on input data is: ')
print(most_specific_hypothesis_coordinates)
print('\n')


def most_general(feature,label,most_specific_hypothesis):

    rectangle_coords = most_specific_hypothesis.copy()

    minimum_x = feature.min(axis=0)
    min_x = minimum_x[0]

    maximum_x = feature.max(axis=0)
    max_x = maximum_x[0]

    minimum_y = feature.min(axis=0)
    min_y = minimum_y[1]

    maximum_y = feature.max(axis=0)
    max_y = maximum_y[1]

    #print(min_x)
    #print(max_x)

    #print(min_y)
    #print(max_y)

    for i in range(len(features)):

      if features[i][0] < most_specific_hypothesis[0] and features[i][0]> min_x:
        rectangle_coords[0] = features[i][0]
        min_x = features[i][0]


      if features[i][0] > most_specific_hypothesis[1] and features[i][0] < max_x:
        rectangle_coords[1] = features[i][0]
        max_x = features[i][0]

      if features[i][1] < most_specific_hypothesis[2] and features[i][1]> min_y:
        rectangle_coords[2] = features[i][1]
        min_y = features[i][1]

      if features[i][1] > most_specific_hypothesis[3] and features[i][1] < max_y:
        rectangle_coords[3] = features[i][1]
        max_y = features[i][1]

    return rectangle_coords


most_general_hypothesis_coordinates = most_general(features,labels,most_specific_hypothesis_coordinates)
print('\nCoordinates of rectangle (x1,x2,y1,y2) describing Most General Hypothesis G based on input data is: ')
print(most_general_hypothesis_coordinates)
print('\n')
