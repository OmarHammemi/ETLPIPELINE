FUNCTION_NAME := dataTransformation
HANDLER := lambda.handler
PACKAGE_NAME := lambda.zip
ROLE := arn:aws:iam::046663258044:role/service-role/data_transformation-role-38asu54h
file := API/lambda.py

.PHONY: package deploy update invoke

package:
	@echo "Packaging Python files..."
	@cd API && zip -q ../$(PACKAGE_NAME) lambda.py

deploy:	
	@echo "Deploying Lambda function..."
	@aws lambda get-function --function-name $(FUNCTION_NAME) > /dev/null 2>&1; \
	if [ $$? -eq 0 ]; then \
		echo "Updating Lambda function..."; \
		aws lambda update-function-code \
			--function-name $(FUNCTION_NAME) \
			--zip-file fileb://$(PACKAGE_NAME); \
	else \
		echo "Creating Lambda function..."; \
		aws lambda create-function \
			--function-name $(FUNCTION_NAME) \
			--runtime python3.8 \
			--role $(ROLE) \
			--handler $(HANDLER) \
			--zip-file fileb://$(PACKAGE_NAME); \
	fi

# invoke:
# 	@echo "Invoking Lambda function..."
# 	@aws lambda invoke \
# 	    --function-name $(FUNCTION_NAME) \
# 	    --payload "{\"Key\":\"value\"}" \
# 	    output.json

build:
	make package && make deploy 

# test:
# 	make build && make invoke