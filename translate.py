import oci
print(f'OCI Client SDK version: {oci.__version__}')

#assuming ashburn endpoint. For other regions, specify appropriate end point
endpoint = "https://language.aiservice.us-ashburn-1.oci.oraclecloud.com"
#Ashburn: https://language.aiservice.us-ashburn-1.oci.oraclecloud.com
#Phoenix: https://language.aiservice.us-phoenix-1.oci.oraclecloud.com
#Frankfurt: https://language.aiservice.eu-frankfurt-1.oci.oraclecloud.com
#London: https://language.aiservice.uk-london-1.oci.oraclecloud.com
#Mumbai: https://language.aiservice.ap-mumbai-1.oci.oraclecloud.com

ai_client = oci.ai_language.AIServiceLanguageClient(oci.config.from_file(profile_name="specialist2-4sdk"),
                                                    service_endpoint=endpoint)


key1 = "doc1"
key2 = "doc2"
text1 = "The Indy Autonomous Challenge is the worlds first head-to-head, high speed autonomous race taking place at the Indianapolis Motor Speedway"
text2 = "OCI will be the cloud engine for the artificial intelligence models that drive the MIT Driverless cars."
target_language = "de" #TODO specify the target language
compartment_id = "ocid1.compartment.oc1..aaaaaaaagwmfwd2pdlllrvfdlkhfrg3wjuo6syt7rk7rauewkjjoe5w7crrq" #TODO Provide your compartmentId here

doc1 = oci.ai_language.models.TextDocument(key=key1, text=text1, language_code="en")
doc2 = oci.ai_language.models.TextDocument(key=key2, text=text2, language_code="en")
documents = [doc1, doc2]

batch_language_translation_details = oci.ai_language.models.BatchLanguageTranslationDetails(documents=documents, compartment_id=compartment_id, target_language_code=target_language)
output = ai_client.batch_language_translation (batch_language_translation_details)
print(output.data)
