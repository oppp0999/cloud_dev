from googleapiclient import discovery

if __name__ == "__main__" :
    notebooks = discovery.build("notebooks", "v1")
    response = notebooks.projects().location().instances().list(parent="projects/{projectId}/locations/{location}").execute()
    print(response)