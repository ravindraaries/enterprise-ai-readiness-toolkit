# Enterprise AI readiness review checklist

Use this during architecture workshops. Record evidence and owners; do not treat checkbox completion as proof of production readiness.

## Cloud migration
- [ ] Identify workload owners, data sensitivity, and dependency maps.
- [ ] Choose migration disposition (including retain/retire where appropriate).
- [ ] Define migration waves, data validation, cutover and rollback gates.

## Application modernization
- [ ] Identify bounded contexts and legacy integration contracts.
- [ ] Select incremental replacement candidates and safe routing boundaries.
- [ ] Verify regression coverage, observability and rollback.

## Custom software development
- [ ] Publish API schemas and versioning policies.
- [ ] Assign service ownership, access controls and secrets management.
- [ ] Implement CI/CD checks, integration tests and release procedures.

## AI server infrastructure
- [ ] Specify inference workload, model sizes and traffic profiles.
- [ ] Benchmark latency, throughput, utilization and cost on candidate hardware.
- [ ] Plan model registry, access controls, telemetry and fallback.

## Network optimization
- [ ] Establish service-to-service latency budgets and error budgets.
- [ ] Measure regional routing, packet loss, bandwidth and congestion.
- [ ] Validate segmentation, failover, encryption and alerting.

## Governance
- [ ] Assign an owner and target date to every gap.
- [ ] Document risks, approvals and rollback responsibility.
- [ ] Review changes with security, compliance and operations teams.
