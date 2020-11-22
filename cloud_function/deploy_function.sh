gcloud functions deploy recent_tweets \
--entry-point=main \
--runtime=python37 \
--trigger-http \
--timeout=65 \
--region=europe-west2 \
--memory=256MB \
--max-instances=1 \
--no-allow-unauthenticated \
--env-vars-file=.env.yaml