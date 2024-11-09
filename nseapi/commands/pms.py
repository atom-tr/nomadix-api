from nseapi.types import MACAddress, BaseCommand
from nseapi.commands.options import pms as spec

__all__ = [
    "USER_PAYMENT",
    "USER_PURCHASE",
    "PMS_PENDING_TRANSACTION",
    "ROOM_SET_ACCESS",
    "ROOM_QUERY_ACCESS",
]


class USER_PAYMENT(BaseCommand):
    """
    Initiates subscriber authorization and payment through PMS. This command verifies room mapping,
    establishes PMS communication, posts access fees to the PMS for the subscriber's room bill, and
    adds the subscriber to the internal database for access. If the subscriber is in the Current
    (active) memory table of the NSE, the Update Cache XML command must follow to correctly update
    the subscriber.

    Required options:

    - USER_NAME (str): Subscriber's username.
    - PASSWORD (str): Subscriber's password.
    - ROOM_NUMBER (str): Room number (Port-Location 'Location' number) of access.
    - MAC_ADDR (str): MAC address of user for post-paid PMS and 2-way PMS.
    - REG_NUMBER (str): Reservation number of hotel guest for Micros Fidelio FIAS compliant Query and Post interface.

    For a complete list of available kwargs options, refer to the USER_PAYMENT method's documentation by running USER_PAYMENT.help().
    """

    _type, _spec, *_ = spec.USER_PAYMENT

    def __init__(
        self,
        user_name: str,
        password: str,
        room_number: str,
        mac_addr: MACAddress,
        reg_number: str,
        *args,
        **kwargs
    ):
        self._transform(
            USER_NAME=user_name,
            PASSWORD=password,
            ROOM_NUMBER=room_number,
            MAC_ADDR=mac_addr,
            REG_NUMBER=reg_number,
            *args,
            **kwargs
        )  # pragma: no cover


class USER_PURCHASE(BaseCommand):
    """
    Initiates a subscriber's e-commerce or special service purchase to be charged via the PMS system.

    Required options:

    - ROOM_NUMBER (str): Room number (Port-Location 'Location' number).
    - ITEM_CODE (str): Code of the item being purchased.
    - ITEM_DESCRIPTION (str): Description of the item.
    - ITEM_AMOUNT (float): Item amount.
    - ITEM_TAX (float): Item tax.
    - ITEM_TOTAL (float): Item total.
    - REAL_NAME (str): Name in the PMS DATABASE. Only needed for 2-way PMS.
    - REG_NUMBER (str): Registration number required for 2-way FIAS PMS.

    For a complete list of available kwargs options, refer to the USER_PURCHASE method's documentation by running USER_PURCHASE.help().
    """

    _type, _spec, *_ = spec.USER_PURCHASE

    def __init__(
        self,
        room_number: str,
        item_code: str,
        item_description: str,
        item_amount: float,
        item_tax: float,
        item_total: float,
        real_name: str,
        reg_number: str,
        *args,
        **kwargs
    ):
        self._transform(
            ROOM_NUMBER=room_number,
            ITEM_CODE=item_code,
            ITEM_DESCRIPTION=item_description,
            ITEM_AMOUNT=item_amount,
            ITEM_TAX=item_tax,
            ITEM_TOTAL=item_total,
            REAL_NAME=real_name,
            REG_NUMBER=reg_number,
            *args,
            **kwargs
        )  # pragma: no cover


class PMS_PENDING_TRANSACTION(BaseCommand):
    """
    Submits a pending PMS transaction to be processed by the PMS Serial Redirector. This command should be sent as a POST to the following address:
    http(s)://NSE_URI/api/pmsRedirector/v1/pendingTransaction.

    Input:

    - TRANSACTION_ID (32 bit unsigned Integer): Used to match commands with PMS_TRANSACTION_RESPONSE messages.
    - DATA (str): The data that will be sent to the attached PMS system. Before sending, the data is framed with an ETX (hex 02) and an STX (hex 03) and appended with a checksum.
    """

    _type, _spec, *_ = spec.PMS_PENDING_TRANSACTION

    def __init__(self, data: str, *arg, **kwargs):
        self._transform(DATA=data, *arg, **kwargs)  # pragma: no cover


class ROOM_SET_ACCESS(BaseCommand):
    """
    Sets room access as per the Administrator's request to the NSE.

    Input:

    - ROOM_NUMBER (str): Room number (Port-Location 'Location' number).
    - ACCESS_MODE (str): Either ROOM_OPEN, ROOM_CHARGE, or ROOM_BLOCK.
    """

    _type, _spec, *_ = spec.ROOM_SET_ACCESS

    def __init__(self, room_number: str, access_mode: str):
        self._transform(
            ROOM_NUMBER=room_number, ACCESS_MODE=access_mode
        )  # pragma: no cover


class ROOM_QUERY_ACCESS(BaseCommand):
    """
    Queries the access status of a room as per the Administrator's request to the NSE.

    Input:

    - ROOM_NUMBER (str): Room number (Port-Location 'Location' number).
    """

    _type, _spec, *_ = spec.ROOM_QUERY_ACCESS

    def __init__(self, room_number: str):
        self._transform(ROOM_NUMBER=room_number)  # pragma: no cover
