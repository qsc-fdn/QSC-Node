from importlib import import_module

TYPENAME_MAP = {
    'transfer': 'TransferTransaction',
    'coinbase': 'CoinBase',
    'latticePK': 'LatticeTransaction',
    'message': 'MessageTransaction',
    'token': 'TokenTransaction',
    'transfer_token': 'TransferTokenTransaction',
    'slave': 'SlaveTransaction',

    'multi_sig_create': 'MultiSigCreate',
    'multi_sig_spend': 'MultiSigSpend',
    'multi_sig_vote': 'MultiSigVote',
}

TYPENAME_PACKAGE = {
    'transfer': 'qsc.core.txs',
    'coinbase': 'qsc.core.txs',
    'latticePK': 'qsc.core.txs',
    'message': 'qsc.core.txs',
    'token': 'qsc.core.txs',
    'transfer_token': 'qsc.core.txs',
    'slave': 'qsc.core.txs',

    'multi_sig_create': 'qsc.core.txs.multisig',
    'multi_sig_spend': 'qsc.core.txs.multisig',
    'multi_sig_vote': 'qsc.core.txs.multisig',

    'proposal_vote': 'qsc.core.txs.proposal',
}


def build_tx(pb_tx_type, *args, **kwargs):
    try:
        tx_class_name = TYPENAME_MAP[pb_tx_type]
        package = TYPENAME_PACKAGE[pb_tx_type]
        tx_module = import_module('.' + tx_class_name, package=package)
        tx_class = getattr(tx_module, tx_class_name)
        return tx_class(*args, **kwargs)

    except(AttributeError, ModuleNotFoundError) as e:  # noqa
        raise ImportError("{} is not defined as a transaction type".format(pb_tx_type))
