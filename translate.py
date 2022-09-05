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

#specify the documents for translation.
document_details = oci.ai_language.models.BatchLanguageTranslationDetails(documents = [
    oci.ai_language.models.TranslationDocument(key="1", source_language_code="en",
                                               target_language_code="fr",
                                               text="I'm gonna make him an offer he can't refuse"),
    oci.ai_language.models.TranslationDocument(key="2", source_language_code="es",
                                               target_language_code="en",
                                               text="Nunca es tarde para aprender")
])

output = ai_client.batch_language_translation(batch_language_translation_details= document_details)
print(output.data)
