from odbAccess import *
odb = openOdb(path='job-11.odb')
fixSet = odb.rootAssembly.instances['PART-1-1'].elementSets['SET-P2']


list_mises = []
for step in odb.steps.values():                             
    for frame in step.frames : 
          sum=0
          totalTime = 0 
          frameTime = frame.frameValue+totalTime   
          field=frame.fieldOutputs['S']
          subField = field.getSubset(region=fixSet) 
          length= len(subField.values) 
          for val in subField.values :
               sum = sum + val.mises
          ave = sum / length
          list_mises.append(ave)
  

print(list_mises[-1])
print('ok')  