elements= {"helium":{"number":1,"weight":22,"Symbol":"he"},"hydrogen":{"number":2,"weight":32,"Symbol":"h20"}}
print(elements)

print(elements['hydrogen']["weight"])

oxygen={"number":3,"weight":23,"Symbol":"o2"}
elements["oxygen"]=oxygen
print(elements)

elements["helium"]["isnoblegas"]=False
elements["hydrogen"]["isnoblegas"]=True
print(elements)
print(elements["hydrogen"]["isnoblegas"])
print(elements["helium"]["isnoblegas"])