import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const MediaRegistryModule = buildModule("MediaRegistryModule", (m) => {
  const mediaRegistry = m.contract("MediaRegistry");

  return { mediaRegistry };
});

export default MediaRegistryModule;