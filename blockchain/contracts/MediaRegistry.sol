// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MediaRegistry {
    struct MediaInfo {
        bool isVerified;
        address creator;
        uint256 timestamp;
        string metadataUri;
    }

    mapping(string => MediaInfo) public registry;

    event MediaRegistered(string pHash, address creator, uint256 timestamp);

    function registerMedia(string memory _pHash, string memory _metadataUri) public {
        require(!registry[_pHash].isVerified, "Media already registered on-chain.");
        
        registry[_pHash] = MediaInfo({
            isVerified: true,
            creator: msg.sender,
            timestamp: block.timestamp,
            metadataUri: _metadataUri
        });

        emit MediaRegistered(_pHash, msg.sender, block.timestamp);
    }

    function verifyMedia(string memory _pHash) public view returns (bool isVerified, address creator, uint256 timestamp, string memory metadataUri) {
        MediaInfo memory media = registry[_pHash];
        return (media.isVerified, media.creator, media.timestamp, media.metadataUri);
    }
}