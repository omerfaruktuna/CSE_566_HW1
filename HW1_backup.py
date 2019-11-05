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
print('\nCoordinates of rectange (x1,x2,y1,y2) describing Most Specific Hypothesis S based on input data is: ')
print(most_specific_hypothesis_coordinates)
print('\n')


def most_general(feature,label,most_specific_hypothesis):

    rectangle_coords = most_specific_hypothesis.copy()
    abc = most_specific_hypothesis.copy()

    a=True
    b=True
    c=True
    d=True

    for i,val in enumerate(label):
        if val == 0:

            if feature[i][0]<rectangle_coords[0] and a:
              first_hypothesis = feature[i].copy()
              a=False
              break

    rectangle_coords[0] = feature[i][0]
    #print(rectangle_coords)



    for i,val in enumerate(label):
        if val == 0:

            if feature[i][0]>rectangle_coords[1] and b:
              first_hypothesis = feature[i].copy()
              b=False
              break

    rectangle_coords[1] = feature[i][0]
    #print(rectangle_coords)


    for i,val in enumerate(label):
        if val == 0:

            if feature[i][1]<rectangle_coords[2] and c:
              first_hypothesis = feature[i].copy()
              c=False
              break

    rectangle_coords[2] = feature[i][1]
    #print(rectangle_coords)

    for i,val in enumerate(label):
        if val == 0:

            if feature[i][1]>rectangle_coords[3] and d:
              first_hypothesis = feature[i].copy()
              d=False
              break

    rectangle_coords[3] = feature[i][1]
    #print(rectangle_coords)



    for i,val in enumerate(feature):
        if label[i] == 0:
          if is_in_rectangle(val,rectangle_coords) :

            abc = enlarge_coordinates(val,abc)


    return abc


most_general_hypothesis_coordinates = most_general(features,labels,most_specific_hypothesis_coordinates)
print('\nCoordinates of rectange (x1,x2,y1,y2) describing Most General Hypothesis G based on input data is: ')
print(most_general_hypothesis_coordinates)
print('\n')
