// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title JokeToken
/// @notice Each joke is a unique, non-fungible, immutable unit of humour.
contract JokeToken is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _ids;

    mapping(uint256 => string) private _punchlines;

    constructor() ERC721("amuse", "HAHA") {}

    function mint(address to, string memory punchline)
        public
        returns (uint256)
    {
        _ids.increment();
        uint256 id = _ids.current();
        _mint(to, id);
        _punchlines[id] = punchline;
        return id;
    }

    /// @notice Tells the joke. Irreversible.
    function tell(uint256 id) public view returns (string memory) {
        require(_exists(id), "amuse: joke does not exist");
        return _punchlines[id];
    }
}
