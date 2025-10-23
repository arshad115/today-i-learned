# API Groups, Domains, and Versioning

Understanding how Kubernetes organizes and names its APIs through domains, groups, and versioning is crucial for working with custom resources and API extensions.

## API vs Group: Key Differences

### API (Application Programming Interface)
- **Definition**: The complete interface for interacting with Kubernetes
- **Scope**: Encompasses all endpoints, operations, and resources
- **Example**: The entire Kubernetes API includes all groups, versions, and resources

### Group (API Group)
- **Definition**: A logical namespace within the API for organizing related resources
- **Scope**: A subset of the API containing related resource types
- **Example**: The `apps` group contains Deployments, ReplicaSets, DaemonSets

### Visual Hierarchy
```
Kubernetes API
├── Core Group (v1)
│   ├── Pod
│   ├── Service
│   └── ConfigMap
├── apps Group
│   ├── v1
│   │   ├── Deployment
│   │   ├── ReplicaSet
│   │   └── DaemonSet
│   └── v1beta1 (deprecated)
├── batch Group
│   ├── v1
│   │   └── Job
│   └── v1beta1
│       └── CronJob
└── networking.k8s.io Group
    └── v1
        ├── NetworkPolicy
        └── Ingress
```

## API Group Structure

Kubernetes APIs are organized hierarchically:

### Core APIs (Legacy)
- **Domain**: No domain (empty string)
- **Group**: No group (empty string) 
- **Examples**: `pods`, `services`, `configmaps`, `secrets`
- **Full API Path**: `/api/v1/pods`

### Named API Groups
- **Domain**: Usually a reverse domain name
- **Group**: Logical grouping of related resources
- **Examples**: `apps/v1`, `networking.k8s.io/v1`, `rbac.authorization.k8s.io/v1`
- **Full API Path**: `/apis/{group}/{version}/{resource}`

## Domain Name Conventions

### Built-in Kubernetes Domains
```yaml
# Core Kubernetes APIs
k8s.io                    # Main Kubernetes domain
kubernetes.io            # Legacy domain (being phased out)
x-k8s.io                 # Experimental features

# Specific API categories
networking.k8s.io        # Network-related APIs
rbac.authorization.k8s.io # RBAC APIs
storage.k8s.io           # Storage APIs
admissionregistration.k8s.io # Admission controllers
apiextensions.k8s.io     # Custom Resource Definitions
```

### Custom Domains
```yaml
# Company/organization domains
mycompany.com
acme.corp
example.org

# Project-specific domains
istio.io
knative.dev
prometheus.io
```

## API Versioning Scheme

Kubernetes uses a structured versioning scheme for APIs, including custom resources.

### Version Format
```
{API Level}{Stability Level}{Version Number}
```

### Components Breakdown

#### API Level
- `v1` = Version 1 (most common)
- `v2` = Version 2
- `v3` = Version 3, etc.

#### Stability Levels

| Level | Description | Use Case | Compatibility |
|-------|-------------|----------|---------------|
| `alpha` | Early development | Experimental features | ⚠️ Breaking changes expected |
| `beta` | More stable | Testing environments | ⚠️ Minor changes possible |
| `stable` (no suffix) | Production ready | Production use | ✅ Backward compatibility guaranteed |

#### Version Numbers within Stability
- **Alpha**: `alpha1`, `alpha2`, `alpha3`, etc.
- **Beta**: `beta1`, `beta2`, `beta3`, etc.
- **Stable**: No additional number (just `v1`, `v2`, etc.)

### Version Progression Examples
```
v1alpha1 → v1alpha2 → v1beta1 → v1beta2 → v1
```

#### Common API Versions
- `v1alpha1` = First alpha version (highly experimental)
- `v1alpha2` = Second alpha version (may have breaking changes from alpha1)
- `v1beta1` = First beta version (more stable, ready for testing)
- `v1beta2` = Second beta version (minor refinements)
- `v1` = First stable version (production ready)

## Group Name Examples and Comparisons

### Core Groups
| Resource | API Group | Version | Full Name |
|----------|-----------|---------|-----------|
| Pod | "" (core) | v1 | v1/Pod |
| Service | "" (core) | v1 | v1/Service |
| Deployment | apps | v1 | apps/v1/Deployment |
| StatefulSet | apps | v1 | apps/v1/StatefulSet |

### Extended Groups
| Resource | API Group | Version | Full Name |
|----------|-----------|---------|-----------|
| NetworkPolicy | networking.k8s.io | v1 | networking.k8s.io/v1/NetworkPolicy |
| Ingress | networking.k8s.io | v1 | networking.k8s.io/v1/Ingress |
| ClusterRole | rbac.authorization.k8s.io | v1 | rbac.authorization.k8s.io/v1/ClusterRole |
| StorageClass | storage.k8s.io | v1 | storage.k8s.io/v1/StorageClass |

## Breaking Down a Full API Name

Let's analyze the full name: `networking.k8s.io/v1/NetworkPolicy`

### Component Breakdown
```
networking.k8s.io/v1/NetworkPolicy
│              │ │  │
│              │ │  └── Resource Name (Kind)
│              │ └───── API Version
│              └──────── API Group
└─────────────────────── Domain
```

### Detailed Parts
1. **Domain**: `k8s.io` - The top-level domain indicating this is a Kubernetes API
2. **Group Prefix**: `networking` - The functional area this API serves
3. **API Group**: `networking.k8s.io` - Complete group identifier
4. **Version**: `v1` - API version (stable release)
5. **Kind/Resource**: `NetworkPolicy` - The specific resource type

## Built-in API Groups

| Group | Purpose | Example Resources |
|-------|---------|-------------------|
| `apps` | Application workloads | Deployment, ReplicaSet, DaemonSet |
| `batch` | Batch processing | Job, CronJob |
| `networking.k8s.io` | Network policies | NetworkPolicy, Ingress |
| `rbac.authorization.k8s.io` | Security & permissions | Role, ClusterRole, RoleBinding |
| `autoscaling` | Auto-scaling | HorizontalPodAutoscaler |
| `storage.k8s.io` | Storage management | StorageClass, VolumeAttachment |
| `apiextensions.k8s.io` | API extensions | CustomResourceDefinition |
| `admissionregistration.k8s.io` | Admission control | ValidatingAdmissionWebhook |
| `certificates.k8s.io` | Certificate management | CertificateSigningRequest |
| `coordination.k8s.io` | Coordination primitives | Lease |
| `discovery.k8s.io` | Service discovery | EndpointSlice |
| `events.k8s.io` | Event handling | Event |
| `node.k8s.io` | Node management | RuntimeClass |
| `policy` | Pod policies | PodDisruptionBudget, PodSecurityPolicy |
| `scheduling.k8s.io` | Scheduling | PriorityClass |

## Custom Resource Example

### CRD Definition
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.mycompany.com
spec:
  group: mycompany.com        # Custom domain
  versions:
  - name: v1
    served: true
    storage: true
  scope: Namespaced
  names:
    plural: databases
    singular: database
    kind: Database
```

### Using the Custom Resource
```yaml
apiVersion: mycompany.com/v1  # Custom group/version
kind: Database                # Custom kind
metadata:
  name: my-database
spec:
  engine: postgresql
  version: "13"
```

## Operator API Examples

Operators are a common pattern in Kubernetes that extend the API with custom resources. Here are real-world operator API examples:

### Database Operators
```yaml
# PostgreSQL Operator (CloudNativePG)
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: postgres-cluster
spec:
  instances: 3
  postgresql:
    parameters:
      max_connections: "200"
  
# MySQL Operator (Oracle)
apiVersion: mysql.oracle.com/v2
kind: InnoDBCluster
metadata:
  name: mysql-cluster
spec:
  secretName: mysql-secret
  tlsUseSelfSigned: true
  instances: 3
```

### Service Mesh Operators  
```yaml
# Istio Operator
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: control-plane
spec:
  values:
    global:
      meshID: mesh1
      network: network1

# Linkerd Operator
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: webapp
spec:
  routes:
  - name: api
    condition:
      method: GET
      pathRegex: "/api/.*"
```

### Monitoring Operators
```yaml
# Prometheus Operator
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: prometheus-main
spec:
  serviceAccountName: prometheus
  serviceMonitorSelector:
    matchLabels:
      team: frontend

# Grafana Operator
apiVersion: integreatly.org/v1alpha1
kind: Grafana
metadata:
  name: grafana
spec:
  ingress:
    enabled: true
  config:
    auth:
      disable_login_form: false
```

### GitOps Operators
```yaml
# ArgoCD Operator
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook
spec:
  project: default
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps.git
    targetRevision: HEAD
    path: guestbook
  destination:
    server: https://kubernetes.default.svc
    namespace: guestbook

# Flux Operator
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: GitRepository
metadata:
  name: podinfo
spec:
  interval: 30s
  ref:
    branch: master
  url: https://github.com/stefanprodan/podinfo
```

### Certificate Management
```yaml
# Cert-Manager Operator
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: example-com-tls
spec:
  secretName: example-com-tls
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  dnsNames:
  - example.com
  - www.example.com

# External Secrets Operator  
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: vault-backend
spec:
  provider:
    vault:
      server: "https://vault.example.com"
      path: "secret"
      auth:
        kubernetes:
          mountPath: "kubernetes"
          role: "example"
```

### Operator API Naming Analysis

Taking the PostgreSQL operator as an example: `postgresql.cnpg.io/v1/Cluster`

```
postgresql.cnpg.io/v1/Cluster
│         │    │  │  │
│         │    │  │  └── Resource Name (Kind)
│         │    │  └───── API Version (stable)
│         │    └──────── Top-level domain (.io)
│         └───────────── Organization (cnpg - CloudNativePG)
└─────────────────────── Technology focus (postgresql)
```

### Common Operator Domains
- `.io` - Most common for open source projects
- `.com` - Commercial/enterprise operators  
- `.dev` - Development-focused tools
- `.k8s.io` - Kubernetes SIG-maintained operators

### Operator Versioning Patterns
```yaml
# Alpha phase - rapid development
postgresql.cnpg.io/v1alpha1
postgresql.cnpg.io/v1alpha2

# Beta phase - stabilizing API
postgresql.cnpg.io/v1beta1  
postgresql.cnpg.io/v1beta2

# Stable phase - production ready
postgresql.cnpg.io/v1
postgresql.cnpg.io/v2       # Major version bump for breaking changes
```

## API Discovery Commands

### List API Groups
```bash
kubectl api-resources --api-group=""           # Core APIs
kubectl api-resources --api-group="apps"       # Apps group
kubectl api-resources --api-group="networking.k8s.io"  # Networking group
```

### Get API Versions
```bash
kubectl api-versions | grep networking
kubectl api-versions | sort
```

### Describe API Resource
```bash
kubectl explain deployment.apps
kubectl explain networkpolicy.networking.k8s.io
```

### Available API groups
```bash
kubectl api-versions
```

### Resources in a group
```bash
kubectl api-resources --api-group=apps
kubectl api-resources --api-group=networking.k8s.io
```

### Preferred version for a group
```bash
kubectl api-versions | grep autoscaling
# Output: autoscaling/v1, autoscaling/v2, autoscaling/v2beta2
# v2 is typically the preferred stable version
```

## Best Practices

### Naming Conventions
1. **Use reverse domain notation**: `mycompany.com` not `com.mycompany`
2. **Be descriptive**: `database.mycompany.com` not `db.mycompany.com`
3. **Avoid conflicts**: Don't use `k8s.io` or `kubernetes.io` domains
4. **Use consistent versioning**: Follow semantic versioning principles

### Group Organization
```yaml
# Good: Logical grouping
networking.mycompany.com     # Network-related resources
storage.mycompany.com        # Storage-related resources
security.mycompany.com       # Security-related resources

# Avoid: Generic grouping
mycompany.com               # Too broad
api.mycompany.com           # Redundant
```

### Versioning Best Practices
1. **Start with alpha** for new APIs
2. **Promote gradually** through stability levels
3. **Maintain backward compatibility** in stable versions
4. **Use semantic versioning** principles
5. **Document breaking changes** clearly between alpha versions

### Migration Path Example
```yaml
# v1alpha1
apiVersion: example.com/v1alpha1
kind: MyResource
spec:
  oldField: value

# v1beta1 (with breaking change)
apiVersion: example.com/v1beta1
kind: MyResource
spec:
  newField: value  # oldField renamed

# v1 (stable)
apiVersion: example.com/v1
kind: MyResource
spec:
  newField: value  # API locked for backward compatibility
```

## Common Patterns

### Multi-Tenant Resources
```yaml
# Tenant-specific groups
tenant1.mycompany.com/v1/Application
tenant2.mycompany.com/v1/Application
```

### Feature-Specific Groups
```yaml
# Feature-based organization
monitoring.mycompany.com/v1/Alert
logging.mycompany.com/v1/LogConfig
backup.mycompany.com/v1/BackupPolicy
```

### Custom Resource Groups with Domain-based Naming
Use reverse domain notation for custom groups:

```yaml
apiVersion: company.com/v1alpha1
kind: MyCustomResource
```

### Examples of Custom Groups
```yaml
# Database operator
apiVersion: postgresql.cnpg.io/v1
kind: Cluster

# Service mesh
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator

# Certificate management
apiVersion: cert-manager.io/v1
kind: Certificate

# Monitoring
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
```

### Group Versioning with Multiple Versions
Groups can have multiple versions simultaneously:

```yaml
# Same group, different versions
apiVersion: autoscaling/v1      # Basic HPA
apiVersion: autoscaling/v2      # Advanced HPA with multiple metrics
apiVersion: autoscaling/v2beta2 # Beta version with experimental features
```

Understanding these naming conventions helps in organizing custom resources, debugging API issues, and maintaining clean API structures in Kubernetes environments.
