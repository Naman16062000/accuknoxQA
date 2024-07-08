1. Start Minikube:
    sh
    minikube start
    
2. Deploy the services:
    sh
    kubectl apply -f k8s.yaml
    

3. Verify the services:
    sh
    kubectl get pods
    kubectl get services
    

4. Access the frontend:
    - For Minikube: minikube service <frontend-service-name>
    - For Kind:
      sh
      kubectl port-forward service/frontend-service 8080:80
      
      Open http://localhost:8080 in your browser.

## Automated Testing

1. Install the requests library:
    sh
    pip install requests
    

2. Run the test script:
    sh
    python test.py
