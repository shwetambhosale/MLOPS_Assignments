

# Deploy on EKS Video Link
[Watch the video](https://drive.google.com/file/d/1vSPsD1rzVJgJWUom30ekS-abKiqOkOpq/view)

---

# Create an EKS Cluster and Deploy the 2048 Game
This guide walks you through the steps to create an EKS cluster and deploy the 2048 game into that cluster.

---

## Task 1: Create an EKS Cluster
1. **Cluster Name**: `<yourname>-eks-cluster-1`  
   **Kubernetes Version**: 1.25

2. **IAM Roles**:  
   - Create an IAM role `eks-cluster-role` with the `AmazonEKSClusterPolicy` attached.  
   - Create another IAM role `eks-node-grp-role` with the following policies attached:  
     - `AmazonEKSWorkerNodePolicy`  
     - `AmazonEC2ContainerRegistryReadOnly`  
     - `AmazonEKS_CNI_Policy`  

3. **VPC and Security**:  
   - Use the default VPC.  
   - Choose 2-3 subnets.  
   - Choose a security group that allows ports 22, 80, and 8080.  

4. **Cluster Endpoint Access**: Public access.

5. For **VPC CNI**, CoreDNS, and kube-proxy, select the default versions.  
   Note: For CNI, choose the default version instead of the latest.

6. Click **Create** and wait for the cluster to show up as **Active** (this takes ~10-12 minutes).

---

## Task 2: Add Node Groups to the Cluster
1. Open the cluster → **Compute** → **Add Node Group**.  
   **Node Group Name**: `<yourname>-eks-nodegrp-1`  

2. Select the IAM role `eks-node-grp-role`.

3. **Configuration**:  
   - AMI: Use the default Amazon Linux 2.  
   - Desired/Minimum/Maximum instances: Set all to `1`.  
   - Enable SSH access. Choose a security group that allows ports 22, 80, and 8080.  

4. Leave all other fields as default and click **Create**.  
   This process will take 2-3 minutes.

---

## Task 3: Authenticate to the Cluster
1. **Update the kubeconfig file**:
   ```bash
   aws eks update-kubeconfig --region <region-code> --name <cluster-name>
   ```
   ```markdown
   Example:
   ```bash
   aws eks update-kubeconfig --region us-east-1 --name unus-eks-cluster-1
   ```

2. **Verify the nodes**:
   ```bash
   kubectl get nodes
   ```

3. **Install the nano editor**:
   ```bash
   sudo yum install nano -y
   ```

---

## Task 4: Create a New Pod for the 2048 Game
1. Create a configuration file:
   ```bash
   nano 2048-pod.yaml
   ```

2. Add the following content:
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
      name: 2048-pod
      labels:
         app: 2048-ws
   spec:
      containers:
      - name: 2048-container
        image: blackicebird/2048
        ports:
          - containerPort: 80
   ```

3. Apply the configuration:
   ```bash
   kubectl apply -f 2048-pod.yaml
   ```

4. Verify the pod:
   ```bash
   kubectl get pods
   ```

---

## Task 5: Setup a Load Balancer Service
1. Create a service configuration file:
   ```bash
   nano mygame-svc.yaml
   ```

2. Add the following content:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
      name: mygame-svc
   spec:
      selector:
         app: 2048-ws
      ports:
      - protocol: TCP
        port: 80
        targetPort: 80
      type: LoadBalancer
   ```

3. Apply the configuration:
   ```bash
   kubectl apply -f mygame-svc.yaml
   ```

4. Verify the service:
   ```bash
   kubectl describe svc mygame-svc
   ```

5. Access the game:
   - Use the DNS name of the Load Balancer (available in the EC2 console).
   - Paste it into your browser to play the 2048 game.

---

## Task 6: Cleanup
1. Delete the pod:
   ```bash
   kubectl delete -f 2048-pod.yaml
   ```

2. Delete the service:
   ```bash
   kubectl delete -f mygame-svc.yaml
   ```

3. Verify the cleanup:
   ```bash
   kubectl get pods
   kubectl get services
   ```
```
